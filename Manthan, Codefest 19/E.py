# https://codeforces.com/contest/1208/problem/E

from sys import stdin, stdout
input = stdin.readline
# print = stdout.write

# every row is independent
# for each column position, we can compute a valid range of original array
# then we just pick the maximum value of this range
# now the problem is how to compute the range maximum value

# range max query: segment tree
# but this is not an arbitrary range, but a sliding window

# We can use multisets/ segment trees/ deques to update the answers corresponding to an array if its L[i],R[i] changes.

# property: a list that can pop left and append right, with max value easy found

# max heap is binary search tree

from heapq import heappop, heappush

n, w = list(map(int, input().split()))
a = [list(map(int, input().split()))[1:] for i in range(n)]


def solve(w, a):
    # for each of the row element,
    # we can compute the column that it is added
    # as well as the column that it is deleted
    from collections import defaultdict
    add = defaultdict(set)
    remove = defaultdict(set)

    for row_index, row in enumerate(a):
        for col_index, element in enumerate(row):
            def compute_index(col_index, len_row, w):
                return col_index, w - len_row + col_index + 1

            add_index, remove_index = compute_index(col_index, len(row), w)
            add[add_index].add((row_index, element))
            if remove_index < w:
                remove[remove_index].add((row_index, element))

        # note we also need to consider the empty element here
        if len(row) < w:
            add[0].add((row_index, 0))
            remove[w - len(row)].add((row_index, 0))
            add[len(row)].add((row_index, 0))
    del a
    # print(add)
    # print(remove)

    cur_sum = 0
    heap = [[] for i in range(n)] # MLE

    removed = [defaultdict(int) for i in range(n)]
    for col in range(w):
        for row_index, element in add[col]:
            if len(heap[row_index]):
                cur_sum -= heap[row_index][0]
            heappush(heap[row_index], -element)
            if len(heap[row_index]):
                cur_sum += heap[row_index][0]
        for row_index, element in remove[col]:
            removed[row_index][element] += 1
            while (removed[row_index][-heap[row_index][0]] != 0):
                removed[row_index][-heap[row_index][0]] -= 1
                if len(heap[row_index]):
                    cur_sum -= heap[row_index][0]
                heappop(heap[row_index])
                if len(heap[row_index]):
                    cur_sum += heap[row_index][0]
        print(-cur_sum, end=" ")


solve(w, a)
print()
