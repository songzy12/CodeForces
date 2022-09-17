# https://codeforces.com/contest/1539/problem/C
# 1. sort the array
# 2. split the array
# 3. sort the gap between the groups
# 4. to see how much gaps can the quota fix
# 5. get the final number

n, k, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

def diff(a):
    res = []
    for i in range(1, len(a)):
        if a[i] - a[i-1] <= x:
            continue
        else:
            res.append(a[i] - a[i-1])
    return res

diffs = diff(a)
diffs.sort()
# print(diffs)

# if no k, then ans would be len(diffs)+1

def consume_quota(diff, x):
    if diff % x == 0:
        return diff // x - 1
    return diff // x

def compute_reduction(diffs, k, x):
    count = 0
    usage = 0
    for diff in diffs:
        if consume_quota(diff, x) + usage <= k:
            usage += consume_quota(diff, x)
            count += 1
        else:
            break
    return count

print(len(diffs)+1 - compute_reduction(diffs, k, x))