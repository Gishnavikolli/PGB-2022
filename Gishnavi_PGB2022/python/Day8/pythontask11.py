#Write a Python program to convert a given list of tuples to a list of strings using map function.
#	Original list of tuples:
#	[('red', 'pink'), ('white', 'black'), ('orange', 'green')]
def tuple_str(lst):
    res = list(map(' '.join, lst))
    return res  
colors = [('black', 'white'), ('blue', 'purple'), ('orange', 'green')]
print("Original list of tuples:",colors)
print("After converting list of tuples to list of strings:",tuple_str(colors))