n, k, m = map(int, raw_input().split())
nums = map(int, raw_input().split())
mods = map(lambda x: x % m, nums)

from collections import Counter
c = Counter(mods)
max_ = max(c.values())
if max_ < k:
    print 'No'
else:
    for key, v in c.items():
        if v == max_:
            tar = key
    ans = []
    for i, num in enumerate(nums):
        if mods[i] == tar:
            ans.append(num)
        
        if len(ans) == k:
            break
    print 'Yes'
    for num in ans:
        print num,
    print




