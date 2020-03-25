#!/usr/bin/python

def isPrime(n):
    if n <= 1: return False
    i = 2
    while i**2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def main():
    n = int(input('Enter a number: '))
    count = 0
    for i in range(1, n + 1):
        if isPrime(i): print i,

if __name__ == '__main__':
    main()
