n, x = map(int, raw_input().split())
nums = map(int, raw_input().split())
nums.sort()

nums = filter(lambda t: t <= x, nums)
# 2 2
# 0 2

# 1 0
# 0
if len(nums) == x + 1:
    print 1
else:
    if x not in nums:
        print x - len(nums) 
    else:
        print x + 1 - len(nums) + 1
