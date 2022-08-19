# https://codeforces.com/contest/1720/problem/C
# https://codeforces.com/blog/entry/106136

def get_min_num_from_square(board, i, j):
    # The minimum number of 1s to eliminate from the corners of the square with offset (i,j)
    # |a|b|
    # |c|d|
    a, b, c, d = board[i][j], board[i][j+1], board[i+1][j], board[i+1][j+1]
    return min(a+b+c, a+b+d, a+c+d, b+c+d)


def get_count_1(board):
    res = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                res += 1
    return res


T = int(input())
for t in range(T):
    R, C = map(int, input().split())
    board = []
    for r in range(R):
        board.append(list(map(int, list(input()))))
    min_num = 3
    for i in range(R-1):
        for j in range(C-1):
            min_num = min(min_num, get_min_num_from_square(board, i, j))
    print(get_count_1(board)-min_num+(1 if min_num else 0))
