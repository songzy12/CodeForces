def count(n, index, length):
    if index == length - 1:
        return 1 if n[index] == '4' else 2
    return (2**(length-index-1) if n[index] == '4' else 2**(length-index)) + \
           count(n, index+1, length)
n = raw_input()
print count(n, 0, len(n))
    
    
