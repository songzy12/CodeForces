# https://codeforces.com/contest/892/problem/B


def compute_killed(n, L):
    killed = 0

    index_to_kill = None
    for i in range(n - 1, -1, -1):
        # check whether i will be killed
        if index_to_kill != None and i >= index_to_kill:
            killed += 1

        # update index_to_kill
        if index_to_kill is None:
            index_to_kill = i - L[i]
        else:
            index_to_kill = min(index_to_kill, i - L[i])
    return killed


if __name__ == "__main__":
    n = int(input())
    L = list(map(int, input().split()))
    print(n - compute_killed(n, L))
