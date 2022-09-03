n = int(raw_input())
a = map(int, raw_input().split())
b = map(int, raw_input().split())

total = sum(a)
max_ = sum(sorted(b)[-2:])

print 'YES' if max_ >= total else 'NO'

