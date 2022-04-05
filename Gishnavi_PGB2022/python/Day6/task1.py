#Define variables for each data type and store respective data
s='Gishnavi'
print(s)
print(type(s))
x=356
print(x)
print(type(x))
a=10
b=20
print(a>b)
print(a==b)
print(a<b)
mylist=["car","bike",10,25.5]
print(mylist)
print(type(mylist))
mytuple=("car","bike",10,25.5)
print(mytuple)
print(type(mytuple))
mydict={"name":"Gishnavi","project":"PGB2022"}
print(mydict)
print(type(mydict))
myset = {"apple", "banana", "cherry"}
print(myset) 
print(type(myset))
# modify the data and identify which data types are mutable and which are immutable
mylist.insert(4,"metro")
print(mylist)
print(" List is Mutable")
#mytuple.insert(4,"metro")
print(mytuple) 
print(" Tuple is immutable")
mydict.popitem()
print(mydict)
print("Dictionary is Mutable")
myset.pop()
print(myset)
print("Set is Mutable")
# Create variables and assign multiple values and override the data types
x=10
y=20
z=30
print(x,y,z)
x=y=z=20
print(x)
print(y)
print(z)
x=y=12
z=6
print(x,y,z)
#Define variable 'a' and store int and string types using + operator and resolve errors if any
#define variable 'b' and sore string and boolean types using + operator and resolve errors if any
#define variable 'c' and sote list and tuple types using + operator and resolve errors if any
name="Gishnavi"
age=7
print("combining the string and int value using + operator ",name+str(age));

k="Gishnavi"
l=True
print("combining the string and bool using + operator ",k+str(l));

m=["a", "b", "c"] 
n=("def")
print("combining the list and tuple using + operator ",m+list(n));
#list
#creating a list
names = ['sam', 'tom', 'jam']
vehicles = ['car', 'bike', 'bus']
print(names)
print(vehicles)
#a. Add an element to the names list
names.append("pam")
print(names)
#c. Copy the names list
names2=names.copy()
print(names2)
#b. Remove all elements from the names list
names2.clear()
print(names2)
#d. Return the number of times the value "jam" appears in the names list
print(names.count("jam"))
#e. Add the elements of cars to the names list
print(names+vehicles)
#f. What is the position of the value "jam
print(names.index("jam"))
#g. Insert the value "ram" as the second element of the names list
names.insert(2,"ram")
print(names)
#h. Remove the second element of the names list
names.pop(2)
print(names)
#i. Remove the "tom" element of the names list
names.remove("tom")
print(names)
#j. Reverse the order of the names list
names.reverse()
print(names)
#k. Sort the cars list 
vehicles.sort()
print(vehicles)

#string
#create a string
msg ="Python Is Procedural Language."
print(msg)
#a.Convert it into upper case
print(msg.upper())
#b.Convert into lower case
print(msg.lower())
#c.Return the number of times a specified value occurs in a string
print(msg.count("Is"))
#d.Return true if the string ends with the specified value
print(msg.endswith("."))
#e.Return True if all characters in the string are in the alphabet
print(msg.isalpha())
#f.Convert the first character of each word to upper case
print(msg.title())
#g.Convert the first character to upper case
print(msg.capitalize())
#h.Search the string for a specified value and returns the position of where it was found
print(msg.find("a"))
#i. Reverse the string with slicing
print(msg[::-1])

#tuple
tuple2=("director",678,"producer",56.7,)
print(tuple2)
#a.Return the number of times a specified value occurs in a tuple
print(tuple2.count("producer"))
#b.Search the tuple for a specified value and returns the position of where it was found
print(tuple2.index("producer"))

#Dictionary
#9.  Create a dictionary with 3 different keys, all with the value '5' using inbuilt method
li =['apple', 'banana', 'orange']
k=5
thisdict = dict.fromkeys(li, k)
print(thisdict)
# create a dictionary
Dict = {"Name": "Tom", "Age": 22, "empid":"3679"}    
print(Dict)
#a. Return the value of the specified key
print(Dict.get('Age'))
#b. Print all key, value pairs
print(Dict)
#c. Remove the element with the specified key
print(Dict.pop('empid'))
print(Dict)
#d. Remove the last inserted key-value pair
print(Dict.popitem())

#set
set={"english","telugu","hindi"}
print(set)
#Add an element to the set
set.add("tamil")
print(set)
#Remove specific element
set.discard("telugu")
print(set)
#create 2 sets x and y
x1={'ceo','coo','cfo'}
y1={'alex','kate','coo'}
print(x1)
print(y1)
#Return a set that contains the items that only exist in set x, and not in set y
print(x1.difference(y1))
#Remove the items that exist in both 
print(x1^y1)
#Return True if no items in set x is present in set y
print(x1.isdisjoint(y1))
#Return True if all items in set x are present in set 
print(y1.issuperset(x1))
#Return True if all items set y are present in set x
print(x1.issuperset(y1))
#Return a set that contains all items from both sets, except items that are present in both sets
print(x1^y1)
#Remove the items that are present in both sets, AND insert the items that is not present in both sets
res=x1^y1   
z = x1.intersection(y1)
res.update(z)
print(res)
#Return a set that contains all items from both sets, duplicates are excluded
print(x1.union(y1))
#Insert the items from set y into set x
x1.update(y1)
print(x1)
