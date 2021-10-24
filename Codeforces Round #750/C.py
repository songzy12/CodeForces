# https://codeforces.com/contest/1582/problem/C
# check the given string, until we found two candidates.
# then for each of the candidate, compute the minimum.


def compute(s, c):    
    i = 0
    j = len(s) - 1
    count = 0
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
            continue
        if s[i] == c:
            i += 1
            count += 1
            continue
        if s[j] == c:
            j -= 1
            count += 1
            continue
        return -1
    return count


t = int(input())
for _ in range(t):
    n = input()
    s = input()
    i = 0
    j = len(s) - 1
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
    if i >= j:
        print(0)
        continue

    t1 = compute(s[i:j + 1], s[i])
    t2 = compute(s[i:j + 1], s[j])
    if t1 == -1 and t2 == -1:
        print(-1)
    elif t1 == -1:
        print(t2)
    elif t2 == -1:
        print(t1)
    else:
        print(min(t1, t2))