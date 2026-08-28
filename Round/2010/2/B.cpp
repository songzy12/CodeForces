/* https://codeforces.com/contest/2/problem/B

There is a square matrix n × n, consisting of non-negative integer numbers. You
should find such a way on it that

    starts in the upper left cell of the matrix;
    each following cell is to the right or down from the current cell;
    the way ends in the bottom right cell.

Moreover, if we multiply together all the numbers along the way, the result
should be the least "round". In other words, it should end in the least possible
number of zeros.

Input

The first line contains an integer number n (2 ≤ n ≤ 1000), n is the size of the
matrix. Then follow n lines containing the matrix elements (non-negative integer
numbers not exceeding 109).

Output

In the first line print the least number of trailing zeros. In the second line
print the correspondent way itself.

Core idea:

1. Find the path with the fewest twos.
2. Find the path with the fewest fives.
3. Choose whichever resulting path has fewer trailing zeroes.
*/

#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>

using namespace std;

const int maxn = 1005;

int matrix[maxn][maxn];

int twos[maxn][maxn];
int fives[maxn][maxn];

char path0[maxn][maxn];
char path2[maxn][maxn];
char path5[maxn][maxn];

void compute_path_two(int n, int twos[maxn][maxn], char path2[maxn][maxn]) {
    const int inf = 0x3f3f3f3f;
    for (int i = 0; i < n; ++i) {
        twos[i][n] = inf;
        twos[n][i] = inf;
    }
    for (int i = n - 1; i >= 0; i--) {
        for (int j = n - 1; j >= 0; j--) {
            if (i == n - 1 && j == n - 1) continue;
            if (twos[i + 1][j] < twos[i][j + 1]) {
                twos[i][j] += twos[i + 1][j];
                path2[i][j] = 'D';
            } else {
                twos[i][j] += twos[i][j + 1];
                path2[i][j] = 'R';
            }
        }
    }
}

void compute_path_zero(int n, int row_zero, char path[maxn][maxn]) {
    for (int i = 0; i < row_zero; ++i) {
        path[i][0] = 'D';
    }
    for (int j = 0; j < n - 1; ++j) {
        path[row_zero][j] = 'R';
    }
    for (int i = row_zero; i < n - 1; ++i) {
        path[i][n - 1] = 'D';
    }
}

void print_path(char path[maxn][maxn]) {
    int i = 0, j = 0;
    while (path[i][j]) {
        putchar(path[i][j]);
        if (path[i][j] == 'R')
            j++;
        else
            i++;
    }
}

int main() {
    int n;
    scanf("%d", &n);
    memset(matrix, 0, sizeof matrix);
    memset(twos, 0, sizeof twos);
    memset(fives, 0, sizeof fives);

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            int x;
            scanf("%d", &x);
            matrix[i][j] = x;
        }
    }

    bool has_zero = false;
    int row_zero = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (matrix[i][j] == 0) {
                has_zero = true;
                row_zero = i;
                // replace 0 for 10
                twos[i][j] = 1;
                fives[i][j] = 1;
            } else {
                int x = matrix[i][j];
                while ((x % 2) == 0) x /= 2, twos[i][j]++;
                while ((x % 5) == 0) x /= 5, fives[i][j]++;
            }
        }
    }

    compute_path_two(n, twos, path2);
    compute_path_two(n, fives, path5);

    if (has_zero && min(twos[0][0], fives[0][0]) > 1) {
        compute_path_zero(n, row_zero, path0);
        puts("1");
        print_path(path0);
    } else {
        if (twos[0][0] < fives[0][0]) {
            printf("%d\n", twos[0][0]);
            print_path(path2);
        } else {
            printf("%d\n", fives[0][0]);
            print_path(path5);
        }
    }
    puts("");
    return 0;
}
