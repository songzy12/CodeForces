n = int(raw_input())
nums = []
for i in range(n):
    nums.append(map(int, raw_input().split()))

pos = []

if n == 1:
    pos = nums[0]
elif n == 2:
    pos = []
    for a in nums[0]:
        for b in nums[1]:
            pos += [a, b, int(str(a)+str(b)), int(str(b) + str(a))]
else:
    pos = []
    for i in range(n):
        nums[i] = map(str, nums[i])

    for a in nums[0]:
        for b in nums[1]:
            for c in nums[2]:
                pos += map(int, [a, b, c, a+b, b+c, c+a, b+a, c+b, a+c,
                                 a+b+c,a+c+b,b+a+c,b+c+a,c+a+b,c+b+a])

i = 1
while i in pos:
    i += 1
print i - 1
        
