# https://codeforces.com/contest/1552/problem/B
#
# Two passes:
# In the first pass, we find the one that are possible to be the winner.
# Then in the second pass, we verify they are indeed the winner.

T = int(input())


def win(r1, r2):
    # whether r1 wins r2
    cnt = 0
    for match in range(5):
        if r1[match] < r2[match]:
            cnt += 1
    return cnt >= 3 

def verify(candidate, rs):
    for r in rs:
        if win(r, candidate):
            return False
    return True

for t in range(T):
    n = int(input())
    rs = []
    for i in range(n):
        r = list(map(int, input().split()))
        rs.append(r)

    candidate = None
    candidate_index = -1
    for i in range(n):
        if candidate is None or win(rs[i], candidate):
            candidate =  rs[i]
            candidate_index = i + 1

    if verify(candidate, rs):
        print(candidate_index)
    else:
        print(-1)
    
