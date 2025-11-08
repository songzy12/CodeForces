#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
int main()
{
	int a[3][2];
	for (int i = 0; i < 3; ++i)
		for (int j = 0; j < 2; ++j)
			cin >> a[i][j];
	bool can = false;
	for (int i = 0; i < 2; ++i)
		for (int j = 0; j < 2; ++j)
			for (int k = 0; k < 2; ++k)
				if (a[1][i] + a[2][j] <= a[0][k] && max(a[1][1 - i], a[2][1 - j]) <= a[0][1 - k])
				{
					can = true;
					i = j = k = 2;
				}
	cout << (can ? "YES" : "NO") << endl;
	return 0;
}