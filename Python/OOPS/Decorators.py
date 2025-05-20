'''

With the help of decorators, we can add additional features to any functions
without changing the function
Decorators are functions that takes another function as an arguement and returns a function

Suppose we want to add a hello and bye message before any function call, we use decorators

A decorator in Python is a way to modify or extend the behavior of a function or method without
changing its actual code. It's like wrapping a gift—you're putting something around the function 
to add or enhance its functionality.

A decorator is just a function that takes another function as an argument, 
does something with it, and returns a new function.

'''

def decorator(function):
    def wrapper():
        print("\nDo something before the function call")
        function()
        print("Do something after the function call\n")
    return wrapper  

# Now, call the decorator by @decorator before any function

@decorator
def f1():
    print("Hello :)")


@decorator
def f2():
    print("How are you")

@decorator
def f3():
    print("Byee")


f1()
f2()
f3()