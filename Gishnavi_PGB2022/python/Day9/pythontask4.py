#4. Write a Python program to remove newline characters from a file
def RemoveNewlinechar(f):
    list = open(f).readlines()
    return [s.rstrip('\n') for s in list]
print(RemoveNewlinechar("Day9/sample.txt"))