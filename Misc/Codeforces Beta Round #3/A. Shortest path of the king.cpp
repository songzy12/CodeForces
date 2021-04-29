#include <cstdio>
#include <cmath>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main() {
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int x[2], y[2];
    for (int i = 0; i < 2; ++i) {
        x[i] = getchar();
        scanf("%d", &y[i]);
        getchar();
    }
    
    int dx = x[1] - x[0], dy = y[1] - y[0];
    bool l = dx < 0;
    bool u = dy > 0;
    
    int l1 = min(abs(dx), abs(dy)); // note the order
    dx = abs(dx) - l1;
    dy = abs(dy) - l1;
    int l2 = dx + dy;
    
    printf("%d\n", l1+l2);
    
    while (l1--) {
        if (l && u) puts("LU");
        else if (l && !u) puts("LD");
        else if (!l && u) puts("RU");
        else puts("RD");
    }
    
    while (dx--) {
        if (l) puts("L");
        else puts("R");
    }
    
    while (dy--) {
        if (u) puts("U");
        else puts("D");
    }
    
    return 0;
}