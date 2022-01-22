

# def msg(n):
#     if n == 0:
#         return
#     print("Hello World")
#     return msg(n-1)
# msg(5)

'''
def print1(n):
    print(n)
    print2(2)


def print2(n):
    print(n)
    print3(3)


def print3(n):
    print(n)
    print4(4)


def print4(n):
    print(n)
    print5(5)


def print5(n):
    print(n)


print1(1)
'''


# def nos(n):
#     if n == 5:
#         print(5)
#         return
#     print(n)
#     nos(n+1)


# nos(1)
'''
ans = 0


def revNo(n):
    global ans
    if n == 0:
        print(ans)
        return
    rem = n % 10
    n = n//10
    ans = ans * 10 + rem

    revNo(n)


print(revNo(7901))
'''
count = 0


def countZeros(n):
    global count
    if n == 0:
        print(count)
        return

    rem = n % 10
    n = n//10
    if rem == 0:
        count += 1
    countZeros(n)


countZeros(101010101010)
