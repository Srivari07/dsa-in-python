

x = 10  # this will be shadowed al line 10


def fun():
    global x
    print(x)  # 10
    x = 20    # local
    print(x)  # 20


print(x)  # 10
fun()  # 20
