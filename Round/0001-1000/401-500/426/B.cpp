#include<iostream>
using namespace std;

int a[26], b[26];

bool valid(int k) {
    int c = 0;
    for (int i = 0; i < 26; ++i) {
        if (a[i] && b[i])
            c++;
    }
    return c <= k;
}

bool valid(string s, int k) {
    for (int i = 0; i < s.size(); ++i) {
        b[s[i]-'A'] += 1;
    }
    for (int i = 0; i < s.size(); ++i) {
        a[s[i]-'A'] += 1;
        if (i > 0)
            b[s[i-1]-'A'] -= 1;
        if (!valid(k))
            return false;
        
    }
    return true;
}

int main() {
    int n, k;
    cin>>n>>k;
    string s;
    cin>>s;
    cout<<(valid(s,k)?"NO":"YES")<<endl;
}