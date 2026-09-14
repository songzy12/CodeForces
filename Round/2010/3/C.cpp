// https://codeforces.com/contest/3/problem/C

#include <iostream>

using namespace std;

bool isWon(char grid[3][3], char player) {
    for (int i = 0; i < 3; ++i) {
        if (grid[i][0] == player && grid[i][1] == player &&
            grid[i][2] == player)
            return true;
    }

    for (int i = 0; i < 3; ++i) {
        if (grid[0][i] == player && grid[1][i] == player &&
            grid[2][i] == player)
            return true;
    }

    if (grid[0][0] == player && grid[1][1] == player && grid[2][2] == player)
        return true;

    if (grid[2][0] == player && grid[1][1] == player && grid[0][2] == player)
        return true;

    return false;
}

char getNextPlayer(char grid[3][3]) {
    int count_O = 0, count_X = 0;
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            if (grid[i][j] == '0')
                count_O++;
            else if (grid[i][j] == 'X')
                count_X++;
        }
    }

    if (count_X == count_O) return 'X';
    if (count_X - count_O == 1) return '0';
    return 'I';
}

bool isFull(char grid[3][3]) {
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            if (grid[i][j] == '.') return false;
        }
    }
    return true;
}

bool isIllegal(char grid[3][3]) {
    if (getNextPlayer(grid) == 'I') return true;
    if (isWon(grid, 'X') && getNextPlayer(grid) == 'X' ||
        isWon(grid, '0') && getNextPlayer(grid) == '0')
        return true;
    return false;
}

string getGameState(char grid[3][3]) {
    if (isIllegal(grid)) return "illegal";
    if (isWon(grid, 'X')) return "the first player won";
    if (isWon(grid, '0')) return "the second player won";
    if (isFull(grid)) return "draw";
    return (getNextPlayer(grid) == 'X') ? "first" : "second";
}

int main() {
    char grid[3][3];
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            cin >> grid[i][j];
        }
    }

    cout << getGameState(grid) << endl;

    return 0;
}
