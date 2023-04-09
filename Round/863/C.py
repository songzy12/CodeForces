# https://codeforces.com/contest/1811/problem/C

# Denote the original array is a_i, the result array is b_i
# b_i = max(a_{i-1}, a_i), b_{i+1} = max(a_i, a_{i+1})
# then min(b_i, b_{i+1}) = min(max(a_{i-1}, a_i), max(a_i, a_{i+1}))
# 0. without loss of generality, suppose a_{i-1} <= a_{i+1}
# 1. if a_i <= a_{i-1}, then info of a_i would be lost in b_i, b_{i+1};
#    setting a_i as min(b_i, b_{i+1}) = min(a_{i-1}, a_{i+1}) = a_{i-1} has no problem.
# 2. if a_{i-1} < a_i <= a_{i+1}, min(b_i, b_{i+1}) = min(a_i, a_{i+1}) = a_i
# 3. if a_i > a_{i+1}, min(b_i, b_{i+1}) = min(a_i, a_i) = a_i


def reconstruct(b):
    return [b[0]] + [min(b[i], b[i + 1]) for i in range(len(b) - 1)] + [b[-1]]


t = int(input())
for _ in range(t):
    n = input()
    b = list(map(int, input().split()))
    print(*reconstruct(b))
