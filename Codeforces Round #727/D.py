# https://codeforces.com/contest/1539/problem/D

# 1. If there is an item which costs 1, then we will not make the answer worse by buying this item.
# 2. If all prices are 2, then we will not make the answer worse by buying the item with max bi.

n = int(input())
items = []
for i in range(n):
    a, b = map(int, input().split())
    items.append([b, a])

items.sort()
# print(items)

head = 0
tail = len(items)-1
count = 0
pay = 0
while head != tail:
    head_need, head_left = items[head]
    tail_need, tail_left = items[tail]
    # print("head, tail:", head, tail)
    if count >= head_need:
        # now we buy head_left count of items[head]
        count += head_left
        pay += head_left
        head += 1
    else:
        if tail_left > head_need - count:
            # now we buy (head_need - count) of items[tail]
            items[tail][1] -= head_need - count
            pay += 2 * (head_need - count)
            count += head_need - count
        else:
            # now we buy tail_left of items[tail]
            count += tail_left
            pay += 2 * tail_left
            tail -= 1
    # print("count, pay:", count, pay)
head_need, head_left = items[head]
if head_need - count >= head_left:
    pay += 2 * head_left
else:
    pay += max(head_need - count, 0) * 2 + \
        head_left - max(head_need - count, 0)
print(pay)
