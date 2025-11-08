#include<iostream>
#include<algorithm>
using namespace std;

const int maxn = 100000;
int a[maxn+5];
int n;

int compute_gcd() {
    int gcd = __gcd(a[0], a[1]);
    for (int i = 2; i < n; ++i)
        gcd = __gcd(gcd, a[i]);
    return gcd;
}

int compute() {
    int gcd = compute_gcd();
    if (gcd > 1)
        return 0;
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        if (a[i] % 2 == 0)
            continue;
        if (i == n - 1) {
            ans += 2;
        } else {
            if (a[i+1] % 2 == 0) 
                ans += 2;
            else 
                ans += 1;
        }
        i++;
    }
    return ans;
}

int main() {
    cin>>n;
    for (int i = 0; i < n; ++i)
        cin>>a[i];
    cout<<"YES"<<endl<<compute()<<endl;
}