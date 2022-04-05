#Write a Python program to crate two empty classes, Student and Marks. 
#Now create some instances and check whether they are instances of the said classes or not.Also, check whether the said classes are subclasses of the built-in object class or not.
class developer:
    pass 
class tester:
    pass 
developer1 = developer()
tester1 = tester()
print(isinstance(developer1, developer))
print(isinstance(tester1, developer))
print(isinstance(tester1, tester)) 
print(isinstance(developer1, tester))
print("Check whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(developer, object))
print(issubclass(tester, object)) 
