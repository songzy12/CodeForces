#include<iostream>
#include<cstdio>
using namespace std;
int main() {
#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
    long long n, a, b, c;
    cin>>n>>a>>b>>c;
    if (a <= b - c) {
        cout<<n/a<<endl;
    } else {
        long long res = 0;
        if (n >= b)
            res += (n - c) / (b - c);
            // (b-c)*(t-1)+b <= n
            // t <= (n-c)/(b-c)
        n -= (b-c) * res;
        res += n / a;
        cout<<res<<endl;
    }
}