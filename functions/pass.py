

"""
https://www.geeksforgeeks.org/pass-by-reference-vs-value-in-python/
"""

# PASS BY OBJECT REFERENCE


def greet(name):
    name = "Chettiyar"
    return (f"Hello {name}")


def hello(name):
    return (f"Hello {name}")


name = "Srivari"
naam = "Chandrababu"
print(greet(naam))
print(hello(naam))
