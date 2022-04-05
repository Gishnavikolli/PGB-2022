#9. Generate 6 digit random secure OTP
import random
otp = random.randint(100000,999999)
print("OTP:",otp)


#10. Generate a random Password which meets the following conditions
#a. Password length must be 10 characters long.
#b. It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.
import random
import string
characters = string.ascii_letters + string.digits + string.punctuation
password = random.sample(characters,6)
password+=random.choice(string.digits)
password+=random.choice(string.punctuation)
password+=random.sample(string.ascii_uppercase,2)
password="".join(password)
print("The random password is:",password)







