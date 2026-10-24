# 1. function can be assign to a variable

def add(x,y):
    return x+y

abcd=add

# 2. function can be assign in a different function 

def process(x,y,func):
    print(x,y,func(x,y))

process(12,13,abcd)

# 3. defining one function in other

def outer():
    print("outer function")
    def inner():
        print("Inner function")
    return inner  # 4. One function can return another function 

func= outer() # giving outer function as output 
func() # giving input function as output 


# example for defining function inside the fuctions: 

def create_function():
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    return add, sub

func1,func2=create_function()

print(func1(12,23))
print(func2(22,12))


# Different types of arguments: 

# 1. Keyword arguments: assign values by using the keywords are called keyword arguments. 

def details(name, age):
    print("Name is", name)
    print("age is",age)

details("Amit",12)
details(age=12, name="Amit")

# 2. default arguments: 

def multiply(x,y,z=20): # here if we don't pass the value of z in the function when we call the function so it will take the value of z as 20
    mul=x*y*z
    return mul

print(multiply(19,68)) # here the default value of z will be taken 

# Variable length arguments: 
def my_sum(a, *b):
    Sum = lambda a, *b: a + sum(b)
    return Sum(a, *b)

print(my_sum(12, 14))
print(my_sum(12, 12, 24, 234, 54, 234))
print(my_sum(12, 1321, 433234, 23, 434, 231, 12, 123, 123))


# Method 2: 

def sum(a,*b):

    Sum=0 

    for element in b:
        Sum+=element
    return Sum+a


print(sum(12,14))
print(sum(12,12,24,234,54,234))
print(sum(12,1321,433234,23,434,231,12,123,123))


# Keywoard length argument 

def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(id=1,name="Jack",qualifications="MBA")



def m1(**x):
    for k, v in x.items():
        print(k,"=",v)

m1(a=10, b=20, c=30)
m1(id=100, name="Subhulaxmi")
