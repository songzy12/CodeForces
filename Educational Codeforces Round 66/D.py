# https://codeforces.com/contest/1175/problem/D

# 1*s1 + 2(s2 -s1) + 3(s3-s2) + k*(sk-s_{k-1})
# k * sk - s_{k-1} - s_1
# here sk = sum()

# we just need to find the k - 1 min prefix sum

n, k = map(int, input().split())
a = list(map(int, input().split()))

prefix_sum = [0]
for t in a:
    prefix_sum.append(prefix_sum[-1] + t)
sk = prefix_sum[-1]
prefix_sum = sorted(prefix_sum[1:-1]) # remember to pop 0 and -1 
print(k*sk - sum(prefix_sum[:k-1]))
