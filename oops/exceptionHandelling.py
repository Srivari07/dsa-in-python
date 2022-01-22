
# https://www.geeksforgeeks.org/python-exception-handling/

a = 5
b = 0
try:
    c = a/b
except(ZeroDivisionError):
    print("Opps!! Error")
else:
    print(c)
finally:
    print("Proogram executed")

# try ,catch/except, finally, throw, throws
