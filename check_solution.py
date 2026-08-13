#!/usr/bin/env python3
"""Run a solution against input and compare with expected output.

Usage:
    python check_solution.py <code_file> <input_file> <expected_output_file>
"""

from __future__ import annotations

import argparse
import difflib
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TIMEOUT_SECONDS = 5


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check whether a solution generates the expected output for a given input."
    )
    parser.add_argument("code_file", help="Path to the source code file")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("expected_output_file", help="Path to the expected output file")
    return parser.parse_args()


def normalize_output(text: str) -> list[str]:
    # Ignore trailing spaces and trailing blank lines for robust comparison.
    lines = [line.rstrip() for line in text.splitlines()]
    while lines and lines[-1] == "":
        lines.pop()
    return lines


def build_command(code_path: Path, work_dir: Path) -> list[str]:
    suffix = code_path.suffix.lower()

    if suffix == ".py":
        return [sys.executable, str(code_path)]

    if suffix in {".cpp", ".cc", ".cxx"}:
        if shutil.which("g++") is None:
            raise RuntimeError("g++ not found; cannot compile C++ source")

        binary_path = work_dir / "solution_bin"
        compile_cmd = [
            "g++",
            "-std=c++17",
            "-O2",
            "-pipe",
            "-s",
            str(code_path),
            "-o",
            str(binary_path),
        ]
        compile_proc = subprocess.run(
            compile_cmd,
            capture_output=True,
            text=True,
        )
        if compile_proc.returncode != 0:
            message = "Compilation failed:\n" + compile_proc.stderr.strip()
            raise RuntimeError(message)
        return [str(binary_path)]

    if os.access(code_path, os.X_OK):
        return [str(code_path)]

    raise RuntimeError(
        f"Unsupported file type: '{suffix or code_path.name}'. "
        "Supported: .py, .cpp/.cc/.cxx, or executable files."
    )


def run_solution(command: list[str], input_text: str, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        input=input_text,
        capture_output=True,
        text=True,
        cwd=str(cwd),
        timeout=TIMEOUT_SECONDS,
    )


def print_diff(expected_lines: list[str], actual_lines: list[str]) -> None:
    diff = difflib.unified_diff(
        expected_lines,
        actual_lines,
        fromfile="expected",
        tofile="actual",
        lineterm="",
    )
    print("Output mismatch. Diff:")
    print("\n".join(diff) or "(no textual diff)")


def main() -> int:
    args = parse_args()

    code_path = Path(args.code_file).resolve()
    input_path = Path(args.input_file).resolve()
    expected_path = Path(args.expected_output_file).resolve()

    for path in (code_path, input_path, expected_path):
        if not path.exists():
            print(f"Error: file not found: {path}", file=sys.stderr)
            return 2

    input_text = input_path.read_text(encoding="utf-8")
    expected_text = expected_path.read_text(encoding="utf-8")

    with tempfile.TemporaryDirectory(prefix="cf_check_") as tmp_dir:
        temp_dir = Path(tmp_dir)

        try:
            command = build_command(code_path, temp_dir)
        except RuntimeError as exc:
            print(f"Error: {exc}", file=sys.stderr)
            return 2

        try:
            proc = run_solution(command, input_text, code_path.parent)
        except subprocess.TimeoutExpired:
            print(f"Time Limit Exceeded ({TIMEOUT_SECONDS}s)")
            return 1

    if proc.returncode != 0:
        print("Runtime Error")
        if proc.stderr.strip():
            print(proc.stderr.strip())
        return 1

    expected_lines = normalize_output(expected_text)
    actual_lines = normalize_output(proc.stdout)

    if expected_lines == actual_lines:
        print("Accepted")
        return 0

    print_diff(expected_lines, actual_lines)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
