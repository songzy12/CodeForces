# https://codeforces.com/blog/entry/67484
# https://codeforces.com/contest/1175/problem/C

# heuristic 2: middle position

# for each point, the k nearest ones are consecutive
# the farest is the two points that are in the end

# for the k+1 th nearest, we just consider k+2 consecutive ones
# and the value is just half the segment length
# the switch position is in the middle of the end points of the k+2 points
# since if we move a little bit to the right, the left end point would be dropped

# the minimum is in the middle of k + 1 elements
# the maximum is in the middle of k + 2 elements

from sys import stdin, stdout
input = stdin.readline
print = stdout.write


def solve(a, k):
    res = (a[k] - a[0]) / 2 # no need to use another array to store a[i:i+k+1]
    x = (a[k] + a[0]) // 2

    for i in range(1, len(a) - k):
        if (a[k + i] - a[i]) / 2 < res:
            res = (a[k + i] - a[i]) / 2
            x = (a[k + i] + a[i]) // 2
    return x


T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(str(solve(a, k))+"\n")
