#Write a Python program to sort a list of tuples using Lambda.
#	Original list of tuples:
#	[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
#	Sorting the List of Tuples:
#	[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
emp_id = [('tom', 180), ('sam', 140), ('jam', 120), ('tam', 150)]
print("Original list of tuples:",emp_id)
emp_id.sort(key = lambda x: x[1])
print("Sorting the List of Tuples:",emp_id) 



