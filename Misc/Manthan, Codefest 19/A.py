from sys import stdin, stdout
input = stdin.readline
print = stdout.write


T  = int(input())
for t in range(T):
    a, b, n = map(int, input().split())
    def solve(a, b, n):
        n %= 3
        if n == 0:
            return a
        elif n == 1:
            return b
        else:
            return a ^ b
    print(str(solve(a, b, n)) + "\n")