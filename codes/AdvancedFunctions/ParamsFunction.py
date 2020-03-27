"""
    We can give Functions params with functions
    
"""


def sum(a, b):
    return a+b


def sub(a, b):
    return a-b


def calculation(f1, f2, operationname):
    if(operationname == "sum"):
        print(f1(2, 3))
    else:
        print(f2(3, 2))


calculation(sum, sub, "sum")  # Functions are parameter in this method
calculation(sum, sub, "sub")
