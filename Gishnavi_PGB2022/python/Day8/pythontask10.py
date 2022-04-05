#Write a Python program to split a given dictionary of lists into list of dictionaries using map function.
#Original dictionary of lists:
#{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
#Split said dictionary of lists into list of dictionaries:	
#[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language':80}]
def dicts(cricket):
    cricket = map(dict, zip(*[[(key, val) for val in value] for key, value in cricket.items()]))
    return list(cricket)
cricket = {'Names': ["virat","dhoni", "rohit"], 'runs': [ 78, 84, 80]}
print("Original dictionary of lists:",cricket)
print("After splitting:",dicts(cricket))


