# https://codeforces.com/contest/1175/problem/E

# 贪心算法 + 优化实现

# That approach is greedy. 
# Let's find such an interval which starts to the left or at x and ends as much to the right as possible. 
# Set x to its right border. Continue until either no interval can be found or y is reached.

# binary lifting / path compression