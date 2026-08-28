/*
 * https://codeforces.com/contest/2/problem/C
 *
 * that is to say the point from where all the three stadiums can be observed.
 * the stadiums should be observed at the same angle.
 * the point with the maximum angle of observation is prefered.
 */

#include <cmath>
#include <cstdio>
#include <iostream>
using namespace std;

double x[3], y[3], r[3];

double distance(double x0, double y0, double x1, double y1) {
    return sqrt((x1 - x0) * (x1 - x0) + (y1 - y0) * (y1 - y0));
}

double error(double px, double py) {
    double res = 0;
    double tan[3];
    for (int i = 0; i < 3; ++i) {
        tan[i] = distance(px, py, x[i], y[i]) / r[i];
    }
    for (int i = 0; i < 3; ++i) {
        res += (tan[i] - tan[(i + 1) % 3]) * (tan[i] - tan[(i + 1) % 3]);
    }
    return res;
}

int main() {
    for (int i = 0; i < 3; ++i) {
        cin >> x[i] >> y[i] >> r[i];
    }

    double px = (x[0] + x[1] + x[2]) / 3;
    double py = (y[0] + y[1] + y[2]) / 3;

    double delta = 1;
    while (delta > 1e-6) {
        if (error(px, py) > error(px + delta, py))
            px += delta;
        else if (error(px, py) > error(px - delta, py))
            px -= delta;
        else if (error(px, py) > error(px, py + delta))
            py += delta;
        else if (error(px, py) > error(px, py - delta))
            py -= delta;
        else
            delta *= 0.7;  // now we can decrease the step length
    }

    if (error(px, py) < 1e-5) {
        printf("%.5f %.5f\n", px, py);
    }
    return 0;
}
