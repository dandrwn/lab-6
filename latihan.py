import math 
def a(x):
    print("a",x**2)

def b(x, y):
    print("b",math.sqrt(x**2 + y**2))

def c(*args):
    print("c",sum(args)/len(args))

def d(s):
    print("c","".join(set(s)))