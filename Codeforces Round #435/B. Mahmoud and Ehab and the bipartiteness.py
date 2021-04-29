import code

n = int(raw_input())
from collections import defaultdict

edges = defaultdict(list)

cnt = [0, 0]

visited = {}

for i in range(n - 1):
    u, v = map(int, raw_input().split())
    edges[u].append(v)
    edges[v].append(u)

def bfs(node, side):
    level = [(node, side)]
    # code.interact(local=locals())
    while level:
        next_level = []

        for _node, _side in level:
            cnt[_side] += 1
            for son in edges[_node]:
                if son in visited:
                    continue
                visited[son] = True
                next_level += (son, 1-side),
        level = next_level
        side = 1-side

visited[1] = True
bfs(1, 0)

# print cnt

print cnt[0] * cnt[1] - n + 1
