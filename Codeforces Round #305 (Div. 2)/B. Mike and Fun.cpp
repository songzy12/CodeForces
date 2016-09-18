#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<cstring>
#include<map>
#include<iomanip>
#define DEBUG
using namespace std;
int a[500][500], n, m;
int b[500];
void print(){
	for(int i=0; i<n; ++i){
		for(int j=0; j<m; ++j)
			cout<<a[i][j]<<" ";
		cout<<" "<<b[i]<<endl;
	}
}
int compute_b(int row){
	int max_row = -1, temp_row = 0;
	for(int j=0; j<m; ++j){
		if(a[row][j] == 1)
			temp_row ++;
		else{
			if(temp_row > max_row)
				max_row = temp_row;
			temp_row = 0;
		}
	}
	if(temp_row > max_row) // in the end
		max_row = temp_row;
	return max_row;
}
int main(){
#ifdef DEBUG
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	ios::sync_with_stdio(false);
	int q;
	cin>>n>>m>>q;
	for(int i=0; i<n; ++i)
		for(int j=0; j<m; ++j)
			cin>>a[i][j];
	for(int i=0; i<n; ++i)
		b[i] = compute_b(i);
	for(int i=0; i<q; ++i){
		int u, v;
		cin>>u>>v;
		a[u-1][v-1] = 1-a[u-1][v-1];
		b[u-1] = compute_b(u-1);
		//print();
		int ans = 0;
		for(int j=0; j<n; ++j)
			if(b[j] > ans)
				ans = b[j];
		cout<<ans<<endl;
	}
	return 0;
}