#include <iostream>
#include <algorithm>

using namespace std;

const int maxn = 1e5;
pair<int, int> k[maxn + 5];
pair<int, int> c[maxn + 5];
int total_k = 0, total_c = 0;

int n, v;
int res_c, res_k;

int max_cap = 0;

void compute()
{
    for (int num_k = 0; num_k <= v; ++num_k)
    { // <= rather than <
        if (num_k > total_k)
            break;
        int num_c = min((v - num_k) / 2, total_c);
        int temp_cap = 0;
        if (num_k > 0)
            temp_cap += k[num_k - 1].first;
        if (num_c > 0)
            temp_cap += c[num_c - 1].first;
        if (temp_cap > max_cap)
        {
            max_cap = temp_cap;
            res_k = num_k;
            res_c = num_c;
        }
    }
}

bool cmp(pair<int, int> p0, pair<int, int> p1)
{
    return p0.first > p1.first;
}

int main()
{
    cin >> n >> v;
    for (int i = 0; i < n; ++i)
    {
        int t, p;
        cin >> t >> p;
        if (t == 1)
        {
            k[total_k++] = make_pair(p, i + 1);
        }
        else
        {
            c[total_c++] = make_pair(p, i + 1);
        }
    }
    sort(k, k + total_k, cmp);
    sort(c, c + total_c, cmp);
    for (int i = 1; i < total_k; ++i)
        k[i].first += k[i - 1].first;
    for (int i = 1; i < total_c; ++i)
        c[i].first += c[i - 1].first;
    compute();
    cout << max_cap << endl;
    for (int i = 0; i < res_k; ++i)
        cout << k[i].second << " ";
    for (int i = 0; i < res_c; ++i)
        cout << c[i].second << " ";
    cout << endl;
    return 0;
}

/* first thought: dp: size of array too large
 * 
 * sort the candidate based on unit capacity
 * then enumerate on the number of type 1
 *
 * WA: num_k <= v
 * TLE: only compute the sum of n candidates once.
 *      only output the index at last
 */