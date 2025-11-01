#include <iostream>
using namespace std;



int main() {
    int a, b, c;
    cin>>a>>b>>c;
    
    int flag = 0;
    if (a < b)
        flag = -1;
    if (a > c)
        flag = 1;
    
    int n;
    cin>>n;
    
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        int t; 
        cin>>t;
        if (flag == 0 && t > b && t < c)
            ans += 1;        
        if (flag == -1 && t < b)
            ans += 1;
        if (flag == 1 && t > c)
            ans += 1;
    }
    cout<<ans<<endl;
}