#include <iostream>
using namespace std;
int main()
{
    int n, t, i;
    cin >> n;
    for (i = 0; i < n; ++i)
    {
        cin >> t;
        if (t == 1)
        {
            cout << -1 << endl;
            break;
        }
    }
    if (i == n)
        cout << 1 << endl;
    return 0;
}
