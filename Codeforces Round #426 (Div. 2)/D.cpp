// dp(k,n): the max cost if we assign first n cakes to k boxes
// k = 1, dp(k,n) = number of distinct values on a prefix
// k > 1, dp(k,n) = max dp(k-1, i-1) + c(i,n)
// c(i,n) is the number of distinct elements in range(i,n)

// maintain a max segment tree with sum dp(k,j-1)+c(j+1,i) in j-th cell
// the answer for dp(k,n) is a prefix query

// i -> i+1: we increase the segment tree values for all cells j 
// such that there is no y in range [j+1,i]

#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <unordered_set>
#include <vector>
#include <cmath>
#include <string>
#include <set>
#include <map>
#include <cstdio>
#include <functional>
#include <random>
#include <ctime>
#include <cassert>
#include <bitset>
#include <unordered_map>
#include <math.h>
#include <queue>

using namespace std;

#define N 35005
#define M 55
#define F 200
mt19937 gen(time(NULL));
#define forn(i, n) for (int i = 0; i < n; i++)
#define fornv(i, n) for (int i = n - 1; i >= 0; i--)
#define pii pair<int, int>
#define forlr(i, l, r) for (int i = l; i <= r; i++)
#define forlrv(i, l, r) for (int i = r; i >= l; i--)
#define debug(...) fprintf(stderr, __VA_ARGS__), fflush(stderr)
#define mp make_pair
typedef long long ll;
typedef unsigned long long ull;
const long double eps = 1e-9;
const int inf = 2e9;
const int mod = 1e9 + 7;
const ll infinity = 2 * 1e18;
#define p p2
#define endl '\n'

int t[4 * N], d[4 * N], w[N];

int dp[M][N];

int n, k;

void build(int k, int u, int l, int r)
{
	if (l == r - 1)
		return void(t[u] = dp[k][l]);

	int m = (l + r) / 2;
	build(k, 2 * u + 1, l, m);
	build(k, 2 * u + 2, m, r);
}

void push(int u, int len)
{
	if (!d[u]) return;

	t[u] += d[u];

	if (len > 1)
		d[2 * u + 1] += d[u], d[2 * u + 2] += d[u];

	d[u] = 0;
}

void update(int u, int l, int r, int L, int R)
{
	push(u, r - l);

	if (l == L && r == R)
	{
		d[u]++;
		push(u, r - l);
		return;
	}

	int m = (l + r) / 2;
	if (L < m)
		update(2 * u + 1, l, m, L, min(m, R));
	else
		push(2 * u + 1, m - l);

	if (R > m)
		update(2 * u + 2, m, r, max(L, m), R);
	else
		push(2 * u + 2, r - m);

	t[u] = max(t[2 * u + 1], t[2 * u + 2]);
}

int get(int u, int l, int r, int L, int R)
{
	if (L >= R) return 0;

	push(u, r - l);

	if (l == L && r == R) return t[u];

	int m = (l + r) / 2, ans = 0;

	if (L < m)
		ans = max(ans, get(2 * u + 1, l, m, L, min(m, R)));
	else
		push(2 * u + 1, m - l);

	if (R > m)
		ans = max(ans, get(2 * u + 2, m, r, max(L, m), R));
	else
		push(2 * u + 2, r - m);

	return ans;
}

int p[N];
map<int, int> last;

void solve(int k)
{
	fill_n(t, 4 * N, 0), fill_n(d, 4 * N, 0);

	build(k - 1, 0, 0, n);

	forn(i, n)
	{
		if (p[i] < i)
			update(0, 0, n, p[i], i);
		dp[k][i] = max(dp[k - 1][i], get(0, 0, n, 0, i));
	}
}


int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
	cin >> n >> k;
	forn(i, n) cin >> w[i];

	forn(i, n)
	{
		p[i] = -1;
		if (last.count(w[i]))
			p[i] = last[w[i]];
		else
			p[i] = 0;

		last[w[i]] = i;
	}

	set<int> s;
	forn(i, n)
	{
		s.insert(w[i]);
		dp[1][i] = s.size();
	}

	for (int i = 2; i <= k; i++) solve(i);

	cout << dp[k][n - 1] << endl;
}