# https://codeforces.com/contest/1/problem/C

from dataclasses import dataclass
from math import degrees, acos, sin, radians


@dataclass
class Point:
    x: float
    y: float


def read_point() -> Point:
    x, y = map(float, input().split())
    return Point(x, y)


def alpha(a2, b2, c2):
    cosA2 = (b2 + c2 - a2)**2 / (4.0 * b2 * c2)
    degree = 2 * degrees(acos(cosA2**0.5))  # geometry
    return degree


def epsilon_div(a, b):
    EPS = 10**(-4)
    return abs(a / b - round(a / b)) < EPS


def find_degree(A, B, C):
    degrees = [360.0 / (i + 1) for i in range(100)]
    for degree in degrees:
        if (epsilon_div(A, degree) and epsilon_div(B, degree) and
                epsilon_div(C, degree)):
            return degree

    return -1


def compute_R2(a2, b2, c2):
    cosA2 = (b2 + c2 - a2)**2 / (4.0 * b2 * c2)
    R2 = a2 / (4.0 * (1 - cosA2))
    return R2


def solve(p0, p1, p2):
    a2 = (p1.x - p2.x)**2 + (p1.y - p2.y)**2
    b2 = (p0.x - p2.x)**2 + (p0.y - p2.y)**2
    c2 = (p1.x - p0.x)**2 + (p1.y - p0.y)**2

    A = alpha(a2, b2, c2)
    B = alpha(b2, c2, a2)
    C = alpha(c2, a2, b2)
    degree = find_degree(A, B, C)

    R2 = compute_R2(a2, b2, c2)
    area = round(360.0 / degree) * 0.5 * sin(radians(degree)) * R2
    return area


if __name__ == '__main__':
    p0 = read_point()
    p1 = read_point()
    p2 = read_point()

    print(f"{solve(p0, p1, p2):.8f}")
