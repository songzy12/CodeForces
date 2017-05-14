#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    int n;
    double h;
    cin>>n>>h;
    double sqrt_n = sqrt(n);
    for (int i = 1; i < n; ++i) {
        cout<<fixed<<setprecision(12)<<sqrt(i) * h / sqrt_n<<" ";
    }
    cout<<endl;
    return 0;
}