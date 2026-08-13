# Codeforces

Solutions for CodeForces Contests: https://codeforces.com

https://codeforces.com/profile/songzy12

https://codeforces.com/contests/with/songzy12

https://clist.by/resource/codeforces.com/

https://clist.by/standings/?resource=1

## Local Checker

Run a solution with a test input and compare against expected output:

```bash
python check_solution.py <code_file> <input_file> <expected_output_file>
```

You can also run with a flagfile:

```bash
python check_solution.py @check.flags
```

Quick start:

```bash
cp check.flags.example check.flags
run.sh
```

`check.flags.example` is tracked as a template, while `check.flags` stays local (`*.flags` is ignored in git).

Example:

```bash
python check_solution.py Round/2010/1/A.py Round/2010/1/testdata/A.in Round/2010/1/testdata/A.out
```
