/* if two or more players have the maximum number of points (say, it equals to m) at the end of the game, 
 * then wins the one of them who scored at least m points first. Initially each player has 0 points. 
 */

#include <cstdio>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int n;
    cin >> n;

    map<string, int> board;
    vector<pair<string, int>> operations;
    string name;
    int score;
    while (n--)
    {
        cin >> name;
        cin >> score;

        if (board.find(name) == board.end())
            board[name] = 0;
        board[name] += score;
        operations.push_back(make_pair(name, board[name]));
    }

    int max_score = 0;
    for (auto &ent : board)
    {
        if (ent.second > max_score)
        {
            max_score = ent.second;
        }
    }

    for (int i = 0; i < operations.size(); ++i)
    {
        name = operations[i].first;
        score = operations[i].second;
        if (score >= max_score && board[name] == max_score)
        {
            cout << name << endl;
            break;
        }
    }
    return 0;
}

/* record the operations, first find out the max socre, 
 * then find out the player achieved max score earlier.
 * 
 * when we find the player achieved max score, 
 * he should have score no less than max score at last.
 */