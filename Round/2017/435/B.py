# https://codeforces.com/contest/862/problem/B

from collections import defaultdict


def bfs(edges):
    """Count the number of nodes on each side of a bipartite graph using BFS.
    Returns a list [count_side_0, count_side_1].
    """
    cnt_nodes = [0, 0]

    node = 1
    side = 0
    visited = {node: True}
    cur_side = [(node, side)]

    while cur_side:
        the_other_side = []

        for _node, _side in cur_side:
            cnt_nodes[_side] += 1
            for the_other_node in edges[_node]:
                if the_other_node in visited:
                    continue
                visited[the_other_node] = True
                the_other_side += (the_other_node, 1 - _side),
        cur_side = the_other_side

    return cnt_nodes


def solve(edges, n):
    cnt_nodes = bfs(edges)
    return cnt_nodes[0] * cnt_nodes[1] - (n - 1)


if __name__ == "__main__":

    n = int(input())

    edges = defaultdict(list)

    for i in range(n - 1):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)

    print(solve(edges, n))
