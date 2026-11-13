# https://codeforces.com/contest/535/problem/C
#
# Height of 1-based: s_i = A + (i-1) x B
#
# Then input l, t, m for each query, return largest r, such that
#   s[l...r] can be eaten by performing m-bite no more than t times.
#
# Here m-bite means decreasing the height of at most m units by 1.


def is_valid(candidate, A, B, t, m, l):
    """Check if s[l...r] can be eaten with m-bite no more than t times."""
    s_l = A + (l - 1) * B
    s_r = A + (candidate - 1) * B
    sum_l_r = (s_l + s_r) * (candidate - l + 1) // 2

    return s_r <= t and sum_l_r <= m * t


def binary_search(lo, hi, A, B, t, m, l):
    ans = -1

    while lo <= hi:
        candidate = lo + (hi - lo) // 2
        # print("lo, hi:", lo, hi)
        # print("candidate:", candidate)
        if is_valid(candidate, A, B, t, m, l):
            ans = candidate
            lo = candidate + 1
        else:
            hi = candidate - 1
    return ans


def compute_max_r(A, B, t):
    """ s_r = A + (r-1) * B <= t
    thus r <= (t - A) // B + 1
    """
    return (t - A) // B + 1


def solve(A, B, t, m, l):
    """Since the heights are non-decreasing, we just need to find the largest r s.t.

    1. s[r] <= t 
    2. the sum of s[l...r] <= m * t

    We can proof that the above conditions are both sufficient and necessary.

    Then, we can find such r using binary search.
    """
    max_r = compute_max_r(A, B, t)
    # print("A, B:", A, B)
    # print("t, m:", t, m)
    # print("l, r:", l, max_r)
    ans = binary_search(l, max_r, A, B, t, m, l)
    return ans


if __name__ == "__main__":
    A, B, n = map(int, input().split())
    for i in range(n):
        l, t, m = map(int, input().split())
        print(solve(A, B, t, m, l))
