# 8. Write a class to handle below exceptions
#	a. ZeroDivisionError
#	b. ImportError
#	c. IndexError
#	d. IndentationError
#	e. ValueError
#	f. Exception
#	g. Raise any exception and handle it properly and use else, finally blocks to print something irrespective of exception
import math
class InvalidBalance(Exception):
  def __str__(self):
    return "Balance must be above 15000."
def validity(balance):
  if balance < 15000:
    raise InvalidBalance
try:
    validity(10000)
except InvalidBalance:
    print("invalid balance")
try:
    import math
    print(math.sqrt(-1))
except ValueError:
    print("Invalid value and value error is raised")
else:
    print("valid value")
try:
    a=[1,2,3,4,5]
    print(a[7])
except IndexError:
    print("out of range error occured")
else:
    print("no error ")
try:
    a=5/0
    print(a)
except ZeroDivisionError:
    print("Zero Division Error occured")
else:
    print("valid division")
try:
    import num
except ImportError:
    print("import error occured")
else:
    print("valid import")
try:
    for i in range(5):
     print(i)
except:
    print(" error occured")
    print(" no error")

