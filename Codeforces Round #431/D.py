n, w, h = map(int, raw_input().split())

class Dancer:
    def __init__(g, p, t):
        self.final = [p, h] if g == 1 else [w, p]
        self.sketch = t - p
        self.collision = []
        self.group = g
    

dancers = []
for i in range(n):
    g, p, t = map(int, raw_input().split())
    dancers.append(Dancer(g, p, t))

from collections import defaultdict

mc1 = defaultdict(list)
mc2 = defaultdict(list)
for dancer in dancers:
    if dancer.group == 1:
        mc2[dancer.sketch].append(dancer)
    else:
        mc1[dancer.sketch].append(dancer)
for dancer in dancers:
    if dancer.group == 1:
        dancer.collision = mc1[dancer.sketch]
    else:
        dancer.collision = mc2[dancer.sketch]

# here is the question: the last dancer may also have changed
