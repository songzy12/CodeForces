#include<iostream>
using namespace std;

int count[10];

int solve(int k, string s) {
    int sum = 0;
    for (int i = 0; i < s.size(); ++i) {
        sum += s[i] - '0';
        count[s[i]-'0']++;
    }
    if (sum >= k)
        return 0;
    int diff = k - sum; // sum < k now
    int ans = 0;
    for (int i = 0; i < 9; ++i) {
        // for index i, each can bring different 9 - i
        int need = diff / (9 - i) + (diff % (9 - i) != 0);
        if (need <= count[i]) {
            ans += need;
            break;
        } else {
            ans += count[i];
            diff -= count[i] * (9 - i);
        }
    }
    return ans;
}

int main() {
    int k;
    string s;
    cin>>k>>s;
    int t = solve(k, s);
    cout<<t<<endl;
    return 0;
}