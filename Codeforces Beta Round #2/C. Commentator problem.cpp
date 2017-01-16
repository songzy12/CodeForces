/* that is to say the point from where all the three stadiums can be observed. 
 * the stadiums should be observed at the same angle. 
 * the point with the maximum angle of observation is prefered.
 */
 
#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

double x[3], y[3], r[3];

double distance(double x0, double y0, double x1, double y1) {
    return sqrt((x1-x0)*(x1-x0) + (y1-y0)*(y1-y0));
}

double error(double dx, double dy) {
    double res = 0;
    double tan[3];
    for (int i = 0; i < 3; ++i)
        tan[i] = distance(dx, dy, x[i], y[i]) / r[i];
    for (int i = 0; i < 3; ++i)
        res += (tan[i] - tan[(i+1)%3])*(tan[i] - tan[(i+1)%3]);
    return res;
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    for (int i = 0; i < 3; ++i)
        cin>>x[i]>>y[i]>>r[i];
    double dx = 0, dy = 0; // remember to initialize
    for (int i =0; i < 3; ++i) {
        dx += x[i] / 3;
        dy += y[i] / 3;
    }
    for (double s = 1; s > 1e-6; ) {
        if (error(dx, dy) > error(dx + s, dy)) 
            dx += s;
        else if (error(dx, dy) > error(dx - s, dy))
            dx -= s;
        else if (error(dx, dy) > error(dx, dy + s))
            dy += s;
        else if (error(dx, dy) > error(dx, dy - s))
            dy -= s;
        else 
            s *= 0.7; // now we can decrease the step length
    }
    if (error(dx, dy) < 1e-5)
        printf("%.5f %.5f\n", dx, dy);
    return 0;
}

/* first thought: if the radio of distances to two fixed node is fixed, then it forms a circle.
 * compute the intersection points and pick the one with the maximum observation angle.
 */
 
/* but it is messy to compute the intersection points directly
 */
 
/* compute the centroid of three centers of circle. 
 * set a initial step length.
 * set the error as squared sum of differences of tan values of the angles.
 * move around the centroid to decrease the error until converge
 */

/* the step length is set to decrease graduately
 * until the precision is under control.
 */