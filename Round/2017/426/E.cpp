// there are no more than \binom{18+9}{9} numbers without leading zeros
// a_1+...+a_n = m, number of non negative solutions: binom{m+n-1}{n-1}

// for each of this number, we check whether it appears in [L, R]

// http://codeforces.com/blog/entry/53567

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

#define N 200005
#define M 20
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

vector<int> L, R;

int n;

int ans = 0;

int num[10];
int keep[10];

inline bool any(int l, int r)
{
	if (l > r) return false;
	for (int i = l; i <= r; i++)
		if (num[i]) return true;
	return false;
}

bool dfs(int pos, bool lf, bool rf)
{
	if (pos == n)
		return true;

	int l = L[pos], r = R[pos];

	if (lf & rf)
	{
		if (l == r)
		{
			if (num[l])
			{
				num[l]--;
				if (dfs(pos + 1, 1, 1))
					return true;
				num[l]++;
			}
			return false;
		}

		if (any(l + 1, r - 1)) return true;

		if (num[l])
		{
			num[l]--;
			if (dfs(pos + 1, 1, 0))
				return true;
			num[l]++;
		}

		if (num[r])
		{
			num[r]--;
			if (dfs(pos + 1, 0, 1))
				return true;
			num[r]++;
		}

		return false;
	}
	else
		if (lf)
		{
			if (any(l + 1, 9)) return true;

			if (num[l])
			{
				num[l]--;
				if (dfs(pos + 1, 1, 0))
					return true;
				num[l]++;
			}

			return false;
		}
		else
			if (rf)
			{
				if (any(0, r - 1)) return true;

				if (num[r])
				{
					num[r]--;
					if (dfs(pos + 1, 0, 1))
						return true;
					num[r]++;
				}

				return false;
			}

	return false;
}

void go(int n, int sum)
{
	if (n == 10)
	{
		memcpy(num, keep, sizeof keep);
		num[0] += sum;

		if (dfs(0, 1, 1)) ans++;
		return;
	}

	for (int i = 0; i <= sum; i++)
	{
		keep[n] = i;
		go(n + 1, sum - i);
	}
}

int main()
{
	ll l, r;
	cin >> l >> r;

	if (l == r)
	{
		cout << 1;
		return 0;
	}

	ll sh_l = l, sh_r = r;

	for (; l; l /= 10)
		L.push_back(l % 10);
	for (; r; r /= 10)
		R.push_back(r % 10);

	n = R.size();

	while (L.size() < n) L.push_back(0);

	reverse(L.begin(), L.end());
	reverse(R.begin(), R.end());

	go(1, n);

	cout << ans << endl;
}