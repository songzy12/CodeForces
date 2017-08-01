#include<iostream>
#include<map>
#include<cmath>
#include<cstdio>
using namespace std;

map<pair<int,int>, bool> dp;

bool valid(int a, int b) {
    if (dp.find({a,b}) != dp.end())
        return dp[{a,b}];
    int rt = cbrt(1.L * a * b);
    if (1.L * rt * rt * rt != 1.L * a * b)
        return dp[{a,b}] = false;
    return dp[{a,b}] = (a % rt == 0 && b % rt == 0);
}

int main() {
    ios::sync_with_stdio(false); // note this
    int n;
    scanf("%d", &n);
    while(n--) {
        int a, b;
        scanf("%d %d", &a, &b);
        if (valid(a, b))
            puts("Yes");
        else
            puts("No");
    }
}