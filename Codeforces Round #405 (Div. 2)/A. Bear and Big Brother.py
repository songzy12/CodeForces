a = [1,3,9,27,81,243,729]
b = [1,2,4,8,16,32,64]
x, y = map(int, raw_input().split())
for i in range(len(a)):
    if x * a[i] > y * b[i]:
        break
print i
