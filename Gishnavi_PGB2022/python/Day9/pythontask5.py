#5. Write a Python program to copy the contents of a file to another file .
import os.path
print(os.getcwd())
if os.path.isfile('Day9/copy.txt'):
    print ("invalid")
else:
    print("valid")
    with open("Day9/sample.txt","r") as f:
        with open("Day9/copy.txt", "w") as f1:
            for line in f:
                f1.write(line)



