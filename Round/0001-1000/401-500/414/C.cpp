#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    string a, b;
    cin>>a>>b;
    sort(a.begin(), a.end());
    sort(b.rbegin(), b.rend());
    string ans = "";
    int n = a.length();
    for (int i = 0; i < n; ++i) {
        if (i % 2 == 0) {
            ans += a[i / 2];
        } else {
            ans += b[i / 2];
        }
    }
    cout<<ans<<endl;
    return 0;
}