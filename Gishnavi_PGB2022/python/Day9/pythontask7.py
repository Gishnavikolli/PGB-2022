#7. A text file named "matter.txt" contains some text, which needs to be displayed such that every next character is separated by a symbol "#". 
#	Write a function definition for hash_display() in Python that would display the entire content of the file matter.txt in the desired format.
#	Example :
#	If the file matter.txt has the following content stored in it :
#	THE WORLD IS ROUND
def hash_display():
    f = open("Day9/sample.txt","r")
    data = f.read()
    for char in data:
        print(char, end="#")
    f.close()
hash_display()