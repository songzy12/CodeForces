# https://codeforces.com/contest/743/problem/D

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

from collections import defaultdict
edge = defaultdict(set)

for _ in range(n - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    edge[u].add(v)
    edge[v].add(u)


class Node:
    def __init__(self, val):
        self.children = []
        self.val = val
        self.sum = self.val
        self.max = None


def build_tree(edge, u):
    node = Node(a[u])
    for v in edge[u]:
        edge[v].remove(u)
        child = build_tree(edge, v)
        node.children.append(child)
    return node


root = build_tree(edge, 0)

# one thing: we can compute the sum value of each child tree
# also, we can compute the maximum subset sum of each child tree

# what if we only check the two largest subset sum of one node?
# it could be the case that for one child, despite the larget sum,
# the second largest sum is stil larger than the second largest subset sum of its farther.

# thus we need to do another dfs, to check the answer with each subtree


def dfs_sum_max(root):
    # compute the subset_sum and subset_max
    for child in root.children:
        dfs_sum_max(child)
        root.sum += child.sum
        root.max = max(root.max, child.max) if root.max != None else child.max
    root.max = max(root.max, root.sum) if root.max != None else root.sum


dfs_sum_max(root)

ans = None


def dfs_ans(root, part):
    # then we find the ans
    global ans
    if part != None:
        ans = (root.sum + part) if ans == None else max(ans, root.sum + part)

    if len(root.children) == 1:
        dfs_ans(root.children[0], part)
        return

    max_set = sorted([[child.max, i]
                      for i, child in enumerate(root.children)], reverse=True)[:2]
    
    for i, child in enumerate(root.children):
        if i == max_set[0][-1]:
            dfs_ans(
                child,
                max_set[1][0] if part == None else max(part, max_set[1][0]))
        else:
            dfs_ans(
                child,
                max_set[0][0] if part == None else max(part, max_set[0][0]))


dfs_ans(root, None)

print(ans if ans != None else "Impossible")