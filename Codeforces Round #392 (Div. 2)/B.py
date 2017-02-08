# encoding=utf8
s = raw_input()

pos = [None] * 4
for i, c in enumerate(s):
    if c != '!':
        pos[i%4] = c

count = {k:0 for k in 'RBYG'}
for i, c in enumerate(s):
    if c == '!':
        count[pos[i%4]] += 1

for t in 'RBYG':
    print count.get(t, 0),
print    

# the color of the n-th bulb equals the color of the (n - 4)-th bulb
# stupid me!
