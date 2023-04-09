# https://codeforces.com/contest/1811/problem/B


def compute_layer(n, x, y):
    left = n // 2
    right = n // 2 + 1
    layer_x = min(abs(x - left), abs(x - right))
    layer_y = min(abs(y - left), abs(y - right))
    # print(left, right, layer_x, layer_y)
    return max(layer_x, layer_y)


t = int(input())
for _ in range(t):
    n, x1, y1, x2, y2 = map(int, input().split())
    l1 = compute_layer(n, x1, y1)
    l2 = compute_layer(n, x2, y2)
    print(abs(l1 - l2))
