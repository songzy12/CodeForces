// https://codeforces.com/contest/3/problem/B
//
// Key Ideas:
// 1. Use prefix sum to easy calculate the total value of selected items.
// 2. Enumerate through possible values of counts of items of each type.

#include <algorithm>
#include <deque>
#include <iostream>
#include <vector>

using namespace std;

vector<int> compute_prefix_sum(const deque<pair<int, int>>& items) {
    vector<int> prefix_sum(items.size() + 1, 0);
    for (int i = 0; i < items.size(); ++i) {
        prefix_sum[i + 1] = prefix_sum[i] + items[i].first;
    }
    return prefix_sum;
}

// Comparison function to sort items by their value in descending order.
bool cmp(pair<int, int> p0, pair<int, int> p1) { return p0.first > p1.first; }

void compute(int space, const deque<pair<int, int>>& kayak,
             const deque<pair<int, int>>& catamaran, int& max_capacity,
             int& best_kayak_count, int& best_catamaran_count) {
    vector<int> prefix_sum_kayak = compute_prefix_sum(kayak);
    vector<int> prefix_sum_catamaran = compute_prefix_sum(catamaran);

    max_capacity = 0;
    best_kayak_count = 0;
    best_catamaran_count = 0;

    int max_catamaran_count = min<int>(catamaran.size(), space / 2);
    for (int cat_count = 0; cat_count <= max_catamaran_count; ++cat_count) {
        int remaining_space = space - 2 * cat_count;
        int kayak_count = min<int>(kayak.size(), remaining_space);
        int current_capacity =
            prefix_sum_catamaran[cat_count] + prefix_sum_kayak[kayak_count];

        if (current_capacity > max_capacity) {
            max_capacity = current_capacity;
            best_catamaran_count = cat_count;
            best_kayak_count = kayak_count;
        }
    }
}

void print_indices(const deque<pair<int, int>>& kayak,
                   const deque<pair<int, int>>& catamaran, int best_kayak_count,
                   int best_catamaran_count) {
    for (int i = 0; i < best_catamaran_count; ++i) {
        cout << catamaran[i].second << " ";
    }
    for (int i = 0; i < best_kayak_count; ++i) {
        cout << kayak[i].second << " ";
    }
    cout << endl;
}

int main() {
    int n, v;
    cin >> n >> v;

    deque<pair<int, int>> kayak;
    deque<pair<int, int>> catamaran;
    for (int i = 0; i < n; ++i) {
        int t, p;
        cin >> t >> p;
        if (t == 1) {
            kayak.push_back(make_pair(p, i + 1));
        } else {
            catamaran.push_back(make_pair(p, i + 1));
        }
    }

    sort(kayak.begin(), kayak.end(), cmp);
    sort(catamaran.begin(), catamaran.end(), cmp);

    int max_capacity;
    int best_kayak_count;
    int best_catamaran_count;
    compute(v, kayak, catamaran, max_capacity, best_kayak_count,
            best_catamaran_count);

    cout << max_capacity << endl;
    print_indices(kayak, catamaran, best_kayak_count, best_catamaran_count);
    return 0;
}
