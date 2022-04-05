import re
global regex
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
class employee:
    def __init__(self, empname, emailId, age):
        self.empname = empname
        self.emailId = emailId
        self.age = age
list = [
    ("gishnavi","gishnavi.k@comakeit.com",21 ),
    ("madiie", ":maddie.j@comakeit.com",-22 ),
    ("gishnavi","gish@123.com" ,19 ),
    ("stefen", "stef.scomakeit.com",17 ),
     ("damon", "demon.s@comakeit.com",15)
]
class DuplicateempnameError(Exception):
    pass
class InvalidAgeError(Exception):
    pass
class InvalidEmailIdError(Exception):
    pass
class UnderageError(Exception):
    pass
dict = {}
for empname, emailId, age in list:
    try:
        if empname in dict:
            raise DuplicateempnameError()
        if age < 0:
            raise InvalidAgeError()
        if age < 16:
            raise UnderageError()
        if not re.fullmatch(regex, emailId): 
            raise InvalidEmailIdError()

    except DuplicateempnameError:
        print("Duplicate empname found:'%s'" % empname)
    except InvalidAgeError:
        print("Invalid age(age is not a positive integer ): %d" % age)
    except UnderageError:
        print("User is underage: %s" % empname)
    except InvalidEmailIdError:
        print("Invalid email address found:'%s'" % emailId)
    else:
        dict[empname] = employee(empname, emailId, age)



