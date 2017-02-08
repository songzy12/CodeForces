# encoding=utf8
n, m, k, x, y = map(int, raw_input().split())

if n == 1:
    T = m
    round_, res = divmod(k, T)
    f11 = round_ + (res > 0)
    fnm = round_ + (res >= n*m)
    fxy = round_ + (res >= y)
    print f11, fnm, fxy
else:
    T = n*m + (n-2)*m
    round_, res = divmod(k, T)

    f11 = round_ + (res>0)
    if n > 2:
        f21 = 2*round_ + (res>m)
        fn_11 = 2*round_ + (2 if res>n*m else 0)
    else:
        f21 = fn_11 = 0
    fnm = round_ + (res >= n*m)
    fxy = (1 if x == 1 or x == n else 2)*round_ + (0 if res < (x-1)*m+y else 1 if (x == n or res < n*m+(n-1-x)*m+y) else 2)
                
    print max(f11, f21, fn_11), fnm, fxy

# T = n·m + (n - 2)·m. If n = 1, then T = m. 
# The maximum number of asked questions to one pupil equals max(f(1, 1), f(2, 1), f(n - 1, 1)).
# The minimum number of asked questions to one pupil equals f(n, m)
