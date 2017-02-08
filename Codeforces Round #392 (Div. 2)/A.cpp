#include <iostream>
using namespace std;

const int maxn = 100;
int a[maxn+5];
int main() {
    int n;
    int max = 0;
    cin>>n;
    for (int i = 0; i < n; ++i) {
        cin>>a[i];
        if (a[i] > max)
            max = a[i];
    }
    int res=  0;
    for (int i = 0; i < n; ++i) 
        res += max-a[i];
    cout<<res<<endl;
    return 0;
}
