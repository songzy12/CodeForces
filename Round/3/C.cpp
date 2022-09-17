#include <iostream>

using namespace std;

char grid[3][3];

bool isWon(int player = 0)
{
    char p = (player == 0) ? 'X' : '0';
    bool temp;
    for (int i = 0; i < 3; ++i)
    {
        temp = true;
        for (int j = 0; j < 3; ++j)
            if (grid[i][j] != p)
            {
                temp = false;
                break;
            }
        if (temp)
            return true;
    }

    for (int i = 0; i < 3; ++i)
    {
        temp = true;
        for (int j = 0; j < 3; ++j)
            if (grid[j][i] != p)
            {
                temp = false;
                break;
            }
        if (temp)
            return true;
    }

    temp = true;
    for (int i = 0; i < 3; ++i)
    {
        if (grid[i][i] != p)
        {
            temp = false;
            break;
        }
    }
    if (temp)
        return true;

    temp = true;
    for (int i = 0; i < 3; ++i)
    {
        if (grid[2 - i][i] != p)
        {
            temp = false;
            break;
        }
    }
    if (temp)
        return true;

    return false;
}

int count[2] = {0};

int getNext()
{
    if (count[0] == count[1])
        return 0;
    if (count[0] - count[1] == 1)
        return 1;
    return -1;
}

bool isIllegal()
{
    if (getNext() == -1)
        return true;
    if (isWon(0) && getNext() == 0 || isWon(1) && getNext() == 1)
        return true;
    return false;
}

int main()
{
    for (int i = 0; i < 3; ++i)
        for (int j = 0; j < 3; ++j)
        {
            cin >> grid[i][j];
            if (grid[i][j] == '0')
                count[1]++;
            else if (grid[i][j] == 'X')
                count[0]++;
        }
    if (isIllegal())
    {
        cout << "illegal" << endl;
    }
    else if (isWon(0))
    {
        cout << "the first player won" << endl;
    }
    else if (isWon(1))
    {
        cout << "the second player won" << endl;
    }
    else if (count[0] + count[1] == 9)
    {
        cout << "draw" << endl;
    }
    else
    {
        cout << ((getNext() == 0) ? "first" : "second") << endl;
    }
    return 0;
}
/*
 * XXX
 * ...
 * 000
 *
 * 000
 * X.X
 * X.X
 */
