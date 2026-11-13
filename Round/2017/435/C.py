# https://codeforces.com/contest/862/problem/C
#
# input x, n
# x, n in range [0, 10**5]
# find a set of n elements whose xor sum is x

def generate_output(n, x):
    """Generator that yields output lines for the XOR solution."""
    if n == 1:
        yield 'YES'
        yield str(x)
    elif n == 2:
        if x == 0:
            yield 'NO'
        else:
            yield 'YES'
            yield f'0 {x}'
    else:
        yield 'YES'

        # Generate numbers 1 to n-3
        numbers = []
        s = 0
        for i in range(1, n - 2):
            numbers.append(i)
            s ^= i

        # Generate the last 3 numbers
        pw = (10**5) << 1
        if s ^ x != 0:
            numbers.extend([pw, pw ^ x ^ s, 0])
        else:
            numbers.extend([pw, pw << 1, pw ^ (pw << 1) ^ x ^ s])

        yield ' '.join(map(str, numbers))


if __name__ == "__main__":
    n, x = map(int, input().split())

    for line in generate_output(n, x):
        print(line)
