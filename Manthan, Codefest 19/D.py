# https://codeforces.com/contest/1208/problem/D

from sys import stdin, stdout
input = stdin.readline
print = stdout.write

# 1. 最右侧的 0 便是当前的最小值
# 2. 然后右侧全部减去这个值，递归
# 但是上面这样耗时太久了

# To find the last index with value zero,
# we can use segment tree to get range minimum query with lazy propagation.

# For every i from N to 1, let's say the value of the si is x. 
# So it means there are k smallest unused numbers whose sum is x.
# We simply put the k+1st number in the output permutation at this i, and continue to move left. 
# This can be implemented using BIT and binary lifting.