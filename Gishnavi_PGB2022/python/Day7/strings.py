#12 Count all letters, digits, and special symbols from a given string
str= "python@123"
alphabets = digits = special = 0
for i in range(len(str)):
    if((str[i] >= 'a' and str[i] <= 'z') or (str[i] >= 'A' and str[i] <= 'Z')):
        alphabets = alphabets + 1
    elif(str[i] >= '0' and str[i] <= '9'):
        digits = digits + 1
    else:
        special = special + 1
print("\nTotal Number of Alphabets in this String :  ", alphabets)
print("Total Number of Digits in this String :  ", digits)
print("Total Number of Special Characters in this String :  ", special)

#13. Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1,
 #then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
str1 = "jammy"
str2 = "kathy"
str3 =''
for i in range(len(str1)):
    str3+=str1[i]
    str3+=str2[-i-1]
print("The string is:",str3)

#14. Write a program to remove special symbols / punctuation from a string
#	Ex : str1 = "/*We are le@arning python@67 fun_da**mentals**"
#	Output: We are learning python fundamentals
punctuation ='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
str="/*We are le@arning python@67 fun_da**mentals**"
no_punc = ""
for char in str:
    if char not in punctuation:
      no_punc = no_punc + char
res = ''.join([i for i in no_punc if not i.isdigit()])      
print (res)

# 15. Write a program to removal all characters from a string except integers
#Input : str1 = 'I am 20 years and and 22 months old'
#Output : 2022
input = 'I am 20 years and and 22 months old'
output = ''.join(c for c in input if c.isdigit())
print(output) 

#16. Write a program to find words with both alphabets and numbers from an input string.
#	Input : str1 = "Sriman25 is Data scientist50 and AI Expert"
#	Output : ['Sriman25','Scientist50']
string = ["Sriman25 is Data scientist50 and AI Expert"]
for i in string:
    for x in i.split(' '):
        if x.isalnum() and not x.isalpha() and not x.isdigit():
            print (x)
