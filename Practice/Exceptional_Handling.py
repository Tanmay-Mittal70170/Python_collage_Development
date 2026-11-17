# Expectional handling

# print("One")
# print("Two")
# try:
#     print(10/0)
# except ZeroDivisionError as z:
#     print("Exception Passed",z)

# print("Four")
# print("Five")


# for j in range(3):
#     try:
#         x=int(input("enter the number 1"))
#         y=int(input("enter the number 2"))
#         print(x/y)

#     except ZeroDivisionError as z:
#         print(z)
#         y=int(input("enter the new number"))

#     except ValueError as v:
#         print(v)
#         x=int(input("enter the number 1"))
#         y=int(input("enter the number 2"))



# try:
#     print("try block")
#     print(10/0)
# except NameError:
#     print("except block")
# finally:
#     print("final block")


# try:
#     print("outer Try block")
    
#     try:
#         print("inner try  block")
#         print(10/0)
#     except NameError:
#         print("inner exception block")
#     finally:
#         print("inner finally block")

# except:
#     print("outer exception block")
# finally:
#     print("outer finally block")

# try:
#     print("Try block")
#     print(10/0)
# except ZeroDivisionError:
#     print("exceptional block")
# else:
#     print("else block")
# finally:
#     print("final block")


# # use of raise keyword:

# try:
#     x=int(input("enter the number"))
#     if x<0:
#         raise ValueError(x)

# except ValueError as v:
#     print("You provoked {}. Please provide positive integer values only".format(v))

