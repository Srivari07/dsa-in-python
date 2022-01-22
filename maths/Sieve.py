

# Sieve of Eratosthenes

'''
https://www.geeksforgeeks.org/sieve-of-eratosthenes/
'''
# false means the no. in array is prime


def sieve(n, primes):
    for i in range(2, n):
        if (primes[i] == False):
            for j in range(i*2, n, i):
                primes[j] = True
    for i in range(2, n):
        if(primes[i] == False):
            print(i, end=" ")


n = 40
primes = [False for i in range(n+1)]
sieve(n, primes)
