'''list = [1, 2, 3]
iterator = iter(list)'''

'''print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))'''

'''for elem in iterator:
    print(elem)

for elem in iterator:
    print(elem)'''

#Замыкание
'''def outer(x):

    def inner(y):
        return x+y
    return inner

closure = outer(10)
print(closure(5))'''

#Decorator
'''def decorator (func):
    def wrappper():
        print("***************************")
        func()
        print("***************************")
    return wrappper()

@decorator
def great():
    print("WELCOME")'''

def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper()

def great():
    return "Murad top"