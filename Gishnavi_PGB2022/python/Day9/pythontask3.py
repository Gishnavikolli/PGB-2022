# Write a Python program that takes a text file as input and returns the number of words of a given text file.
#	Note: Some words can be separated by a comma with no space.
def wordcount(file):
   with open(file) as f:
       txt = f.read()
       txt.replace(",", " ")
       return len(txt.split(" "))
f = open("Day9/sample.txt", "r")
print(wordcount("Day9/sample.txt"))