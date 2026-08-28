// https://codeforces.com/contest/625/problem/A

#include <cstdio>
#include <iostream>

using namespace std;

int main() {
    long long n, a, b, c;
    cin >> n >> a >> b >> c;
    if (a <= b - c) {
        cout << n / a << endl;
    } else {
        long long res = 0;

        // glass bottles first
        if (n >= b) res += (n - c) / (b - c);
        // plastic bottles next
        n -= (b - c) * res;
        res += n / a;

        cout << res << endl;
    }
}