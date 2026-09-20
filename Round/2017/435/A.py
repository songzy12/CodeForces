# https://codeforces.com/contest/862/problem/A


def solve(nums, x):
    count_less = len(list(filter(lambda t: t < x, nums)))

    if x not in nums:
        return x - count_less
    else:
        return x - count_less + 1


if __name__ == "__main__":
    n, x = map(int, input().split())
    nums = list(map(int, input().split()))
    print(solve(nums, x))
