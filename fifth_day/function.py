def square(x):
    return x*x

print(square(4))
print("h"*5)
def response():
    a, b, c = 10, 20, 30
    return a, b, c  # returns a tuple (10, 20, 30)

temp = response()
print(temp)  
a,b,c = response()
print(a,b,c)

cube = lambda x: x*x*x
print(cube(3))
def print_kwargs(**kwargs):
    print("No arguments passed")
print_kwargs(name="John", power="Python")
print_kwargs(name="John")

