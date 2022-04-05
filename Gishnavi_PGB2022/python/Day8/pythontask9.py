#Write a Python program to sort a list of dictionaries by color using Lambda.
#Original list of dictionaries :
#[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
#Sorting the List of dictionaries :
#[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

models = [{'make':'dell', 'model':216, 'color':'silver'}, {'make':'hp', 'model':'2', 'color':'Gold'}, {'make':'lenevo', 'model': 7, 'color':'Blue'}]
print("Original list of dictionaries :",models)
sorted_models = sorted(models, key = lambda x: x['color'])
print("Sorting the List of dictionaries :",sorted_models)


