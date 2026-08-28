// https://codeforces.com/contest/3/problem/A

#include <cmath>
#include <cstdio>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

vector<string> compute_path(int dx, int dy) {
    vector<string> path;
    while (dx != 0 && dy != 0) {
        if (dx > 0 && dy > 0) {
            path.push_back("RU");
            --dx;
            --dy;
        } else if (dx > 0 && dy < 0) {
            path.push_back("RD");
            --dx;
            ++dy;
        } else if (dx < 0 && dy > 0) {
            path.push_back("LU");
            ++dx;
            --dy;
        } else if (dx < 0 && dy < 0) {
            path.push_back("LD");
            ++dx;
            ++dy;
        }
    }
    while (dx != 0) {
        if (dx > 0) {
            path.push_back("R");
            --dx;
        } else {
            path.push_back("L");
            ++dx;
        }
    }
    while (dy != 0) {
        if (dy > 0) {
            path.push_back("U");
            --dy;
        } else {
            path.push_back("D");
            ++dy;
        }
    }
    return path;
}

void print_path(vector<string> path) {
    for (const string& step : path) {
        puts(step.c_str());
    }
}

int main() {
    int x[2], y[2];
    for (int i = 0; i < 2; ++i) {
        x[i] = getchar();
        scanf("%d", &y[i]);
        getchar();
    }

    int dx = x[1] - x[0];
    int dy = y[1] - y[0];
    printf("%d\n", max(abs(dx), abs(dy)));

    vector<string> path = compute_path(dx, dy);
    print_path(path);

    return 0;
}