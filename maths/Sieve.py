

# Sieve of Eratosthenes
# TC : O(n log(log(n))

def foo(n):
    arr=[]
    dp=[True]*(n+1)
    
    for i in range(2,int(n**0.5)+1):
        if dp[i]==True:
            for j in range(i*i,n+1,i):
                dp[j]=False

    for i in range(2,n+1):
        if dp[i]==True:
            arr.append(i)
            
    return arr


n = 10**6
print(foo(n))
