n = int(raw_input())
nums = map(int, raw_input().split())
def check():
    return n % 2 == 1 and nums[0] % 2 == 1 and nums[-1] % 2 == 1
print 'Yes' if check() else 'No'
