n, k = [int(x) for x in raw_input().split()]

def check():
    return (n / k) % 2 == 1

print "YES" if check() else "NO"
