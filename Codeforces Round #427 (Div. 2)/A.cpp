#include<iostream>
using namespace std;
int main() {
    int n,v1,v2,t1,t2;
    cin>>n>>v1>>v2>>t1>>t2;
    int time1 = v1*n+2*t1;
    int time2 = v2*n+2*t2;
    if (time1 < time2) {
        cout<<"First"<<endl;
    } else if (time1 > time2) {
        cout<<"Second"<<endl;
    } else {
        cout<<"Friendship"<<endl;
    }
    return 0;
}