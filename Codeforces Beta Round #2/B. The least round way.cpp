#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

pair<int, int> get_zeros(int x) {
    pair<int, int> t = make_pair(0, 0);
    while (x % 2 == 0) {
        x /= 2;
        t.first++;
    }
    while (x % 5 == 0) {
        x /= 5;
        t.second++;
    }
    return t;
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int n;
    cin>>n;
    vector<vector<pair<int, int>> > matrix;
    for (int i = 0; i < n; ++i) {
        vector<pair<int, int>> row;
        for (int j = 0; j < n; ++j) {
            int x;
            cin>>x;
            row.push_back(get_zeros(x));
        }
        matrix.push_back(row);
    }
    // now we want to find the minimum sum of elements along the path
    vector<vector<char> > path = vector<vector<char> >(n, vector<char>(n, 'X'));
    for (int i = n - 1; i >= 0; i--) {
        for (int j = n - 1; j >= 0; j--) {
            if (i == n - 1 && j == n - 1)
                continue;
            if (i == n - 1) {
                path[i][j] = 'R';
                matrix[i][j].first += matrix[i][j + 1].first;
                matrix[i][j].second += matrix[i][j + 1].second;
                continue;
            }
            if (j == n - 1) {
                path[i][j] = 'D';
                matrix[i][j].first += matrix[i + 1][j].first;
                matrix[i][j].second += matrix[i + 1][j].second;
                continue;
            }
            
            if (min(matrix[i + 1][j].first, matrix[i + 1][j].second) < 
                min(matrix[i][j + 1].first, matrix[i][j + 1].second)) {
                path[i][j] = 'D';
                matrix[i][j].first += matrix[i + 1][j].first;
                matrix[i][j].second += matrix[i + 1][j].second;
            } else {
                path[i][j] = 'R';
                matrix[i][j].first += matrix[i][j + 1].first;
                matrix[i][j].second += matrix[i][j + 1].second;
            }
        }
    }
    cout<<min(matrix[0][0].first, matrix[0][0].second)<<endl;
    int i = 0, j = 0;
    while (path[i][j] != 'X') {
        cout<<path[i][j];
        if (path[i][j] == 'R')
            j++;
        else 
            i++;
    }
    cout<<endl;
    return 0;
}

/* no only 10 will contribute to tailing zeros,
 * we should count the corresponding 2 and 5
 */
 
 /* TLE */