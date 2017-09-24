x = raw_input()

def is_palindrome(x):
    i = 0
    j = len(x) - 1
    while i < j:
        if x[i] != x[j]:
            return False
        i += 1
        j -= 1
    return True

def is_quasi(x):
    for i in range(len(x)+1):
        if is_palindrome('0'*i + x):
            return True
    return False

print 'YES' if is_quasi(x) else 'NO'
