n = int(raw_input())
nums = map(int, raw_input().split())
def check():
    for num in nums:
        if num % 2:
            return True
    return False
print "First" if check() else "Second"
