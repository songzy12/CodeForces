#include <iostream>
#include <cstdio>
#include <cstring>

// cnt[p][x][y] = cnt[p][x - 1][y] + cnt[p][x][y - 1] - cnt[p][x - 1][y - 1] + (the number of stars in the point (x;y) with the

using namespace std;

const int maxn = 100000;
const int maxc = 10;
const int maxx = 100;
const int maxy = 100;
int s[maxx+1][maxy+1][maxc+1];
int c;

int bright(int t, int tx, int ty) {
    int ans = 0;
    for (int i = 0; i <= maxc; ++i)
        ans += s[tx][ty][i] * ((i+t) % (c+1));
    return ans;
} 

int solve(int t, int x1, int y1, int x2, int y2) {
    int ans = 0;
    for (int tx = x1; tx <= x2; ++tx)
        for (int ty = y1; ty <= y2; ++ty)
            ans += bright(t, tx, ty);
    return ans;
}

int main() {
    int n, q;
    scanf("%d %d %d", &n, &q, &c);
    int x, y, s0;
    memset(s, 0, sizeof s);
       
    for (int i = 0; i < n; ++i) {
        scanf("%d %d %d", &x, &y, &s0);        
        s[x][y][s0]++;
    }
   
    int t, x1, y1, x2, y2;
    for (int i = 0; i < q; ++i) {
        scanf("%d %d %d %d %d", &t, &x1, &y1, &x2, &y2);
        t %= (c+1);
        printf("%d\n", solve(t, x1, y1, x2, y2));
    }
}