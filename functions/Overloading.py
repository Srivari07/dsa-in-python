
"""
https://www.geeksforgeeks.org/python-method-overloading/
"""

from multipledispatch import dispatch


@dispatch(int)
def fun(a):
    print(a+0)


@dispatch(str)
def fun(name):
    print("Hello " + name)


fun(7)
fun("srivari")

#   this is done using compile time
