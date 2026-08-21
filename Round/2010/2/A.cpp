// https://codeforces.com/contest/2/problem/A

#include <cstdio>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    map<string, int> board;
    vector<pair<string, int>> operations;
    string name;
    int score;
    while (n--) {
        cin >> name;
        cin >> score;

        if (board.find(name) == board.end()) board[name] = 0;
        board[name] += score;
        operations.push_back(make_pair(name, board[name]));
    }

    int max_score = 0;
    for (auto& ent : board) {
        if (ent.second > max_score) {
            max_score = ent.second;
        }
    }

    for (int i = 0; i < operations.size(); ++i) {
        name = operations[i].first;
        score = operations[i].second;
        if (score >= max_score && board[name] == max_score) {
            cout << name << endl;
            break;
        }
    }
    return 0;
}
