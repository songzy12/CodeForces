// https://codeforces.com/contest/3/problem/D
//
// Idea:
// 1. Initially replace every ? with ).
// 2. Track prefix balance.
// 3. If balance becomes negative, convert the previously seen ? with maximum
// saving closeCost - openCost into (.
// 4. If no such ? exists, answer is impossible.
// 5. At the end, balance must be zero.

#include <algorithm>
#include <iostream>
#include <optional>
#include <queue>
#include <string>
#include <utility>
#include <vector>

using namespace std;
using Candidate = pair<long long, int>;

optional<pair<long long, string>> solve(
    const string& inputSequence,
    const vector<pair<long long, long long>>& costs) {
    string sequence = inputSequence;
    priority_queue<Candidate> candidates;
    long long answer = 0;
    int balance = 0;
    int costIndex = 0;

    for (int index = 0; index < static_cast<int>(sequence.size()); ++index) {
        if (sequence[index] == '(') {
            ++balance;
        } else if (sequence[index] == ')') {
            --balance;
        } else {
            const auto [openCost, closeCost] = costs[costIndex++];
            sequence[index] = ')';
            answer += closeCost;
            --balance;
            candidates.push({closeCost - openCost, index});
        }

        if (balance < 0) {
            if (candidates.empty()) {
                return nullopt;
            }

            const auto [saving, indexToOpen] = candidates.top();
            candidates.pop();
            sequence[indexToOpen] = '(';
            answer -= saving;
            balance += 2;
        }
    }

    if (balance != 0) {
        return nullopt;
    }

    return make_pair(answer, sequence);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string sequence;
    cin >> sequence;

    int costCount = count(sequence.begin(), sequence.end(), '?');
    vector<pair<long long, long long>> costs(costCount);
    for (int i = 0; i < costCount; ++i) {
        cin >> costs[i].first >> costs[i].second;
    }

    const auto result = solve(sequence, costs);
    if (!result) {
        cout << -1 << '\n';
        return 0;
    }

    cout << result->first << '\n' << result->second << '\n';
    return 0;
}
