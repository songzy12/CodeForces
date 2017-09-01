r, d = map(int, raw_input().split())
n = int(raw_input())
circles = []
for i in range(n):
    circles.append(map(int, raw_input().split()))

import math

def check():
    num = 0
    for xi, yi, ri in circles:
        if (r + ri - d <= math.sqrt(xi*xi + yi*yi) <= r - ri):
            num += 1
    return num

print check()
