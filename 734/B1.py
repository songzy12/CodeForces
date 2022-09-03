from collections import defaultdict

T = int(input())

for t in range(T):
    s = input()

    visited = defaultdict(int)
    count = 0
    for c in s:
        visited[c] += 1
        if visited[c] > 2:
            continue
        count += 1
    print(count // 2)