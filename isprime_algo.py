'''
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
            break
    return True
'''

def isPrime(n):
    i = 2
    while True:
        if n % i == 0:
            return False
            break
        i += 1
        if i == n:
            return True
            break
# Tests....
print(isPrime(7)) # Should output True
print(isPrime(143)) # Should output False
print(isPrime(790003)) # Should output True
