/*
There is a square matrix n × n, consisting of non-negative integer numbers. You should find such a way on it that

    starts in the upper left cell of the matrix;
    each following cell is to the right or down from the current cell;
    the way ends in the bottom right cell. 

Moreover, if we multiply together all the numbers along the way, the result should be the least "round". In other words, it should end in the least possible number of zeros.
Input

The first line contains an integer number n (2 ≤ n ≤ 1000), n is the size of the matrix. Then follow n lines containing the matrix elements (non-negative integer numbers not exceeding 109).
Output

In the first line print the least number of trailing zeros. In the second line print the correspondent way itself.
Examples
Input

3
1 2 3
4 5 6
7 8 9

Output

0
DDRR
*/

#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
using namespace std;

const int maxn = 1005;
bool has_zero = false;
int line = 0;

int matrix[maxn][maxn][2];
bool path[maxn][maxn][2];

int main()
{
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int n;
    scanf("%d", &n);
    memset(matrix, 0, sizeof matrix); // use sizeof rather than loop to init, still TLE
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            int x;
            scanf("%d", &x);
            // this is the reason for TLE!!!
            // what if x == 0? should treat carefully.
            if (!x)
            {
                has_zero = true;
                line = i;
                matrix[i][j][0]++; // replace 0 for 10
                matrix[i][j][1]++;
            }
            else
            {
                while ((x % 2) == 0)
                    x /= 2, matrix[i][j][0]++;
                while ((x % 5) == 0)
                    x /= 5, matrix[i][j][1]++;
            }
        }
    }

    // now we want to find the minimum sum of elements along the path
    const int inf = 0x3f3f3f3f;
    for (int i = 0; i < n; ++i)
        matrix[i][n][0] = matrix[i][n][1] = matrix[n][i][0] = matrix[n][i][1] = inf;
    for (int i = n - 1; i >= 0; i--)
    {
        for (int j = n - 1; j >= 0; j--)
        {
            if (i == n - 1 && j == n - 1)
                continue;
            for (int k = 0; k < 2; ++k)
            {
                // use k in [0, 1] rather than explicitly, still TLE
                path[i][j][k] = matrix[i + 1][j][k] > matrix[i][j + 1][k];
                matrix[i][j][k] += min(matrix[i + 1][j][k], matrix[i][j + 1][k]); // use min rather than if, still TLE.
            }
        }
    }

    if (has_zero && min(matrix[0][0][0], matrix[0][0][1]) > 1)
    {
        // there is no path containing containing no 2 or 5
        // the path is always the right path
        // the number is 1 or 0
        puts("1");
        // print any path containing that 0
        for (int i = 0; i < line; ++i)
            putchar('D');
        for (int j = 0; j < n - 1; ++j)
            putchar('R');
        for (int i = line; i < n - 1; ++i)
            putchar('D');
    }
    else
    {
        printf("%d\n", min(matrix[0][0][0], matrix[0][0][1]));
        int i = 0, j = 0;
        if (matrix[0][0][0] < matrix[0][0][1])
        {
            while (i != n - 1 || j != n - 1)
            {
                putchar(path[i][j][0] ? 'R' : 'D');
                if (path[i][j][0])
                    j++;
                else
                    i++;
            }
        }
        else
        {
            while (i != n - 1 || j != n - 1)
            {
                putchar(path[i][j][1] ? 'R' : 'D');
                if (path[i][j][1])
                    j++;
                else
                    i++;
            }
        }
    }
    puts(""); // use puts, putchar, printf to replace cout,
    return 0;
}

/* no only 10 will contribute to tailing zeros,
 * we should count the corresponding 2 and 5
 */

/* the reason for TLE is 
 * while(0 % 2 == 0) 0 /= 2;
 */

/* treat the zero situation differently? too messy?
 */

/* Replace all 0 by 10 and use the method described above. 
 * For paths containing zeroes the result will contain at least one zero at the end. 
 * If the method returned a number without zeroes at the end, the corresponding path is the answer, 
 * else any path containing zeroes is the answer.
 */

/* another way: we can use 0x3f3f3f3f to represent infinity
 */

/* if has_zero == true rather than has_zero = true
 */

/* algorithm is not right
 * should consider 2 and 5 seperately
 * only combine when output
 */

/* change from pair to int, vector to array
 */