#1. Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both 
#addition and subtraction in a single return call.
def calculation(a, b):
    add = a + b
    sub = a - b
    return add, sub
result = calculation(200,100)
print("The result is:",result)

#2. Write a program to create a function show_employee() using the following conditions.
#	a. It should accept the employee’s name and salary and display both.
#	b. If the salary is missing in the function call then assign default value 9000 to salary
def show_employee(emp_name,emp_salary=9000):
    print("employee:",emp_name)
    print("salary:",emp_salary)
show_employee("gishnavi")

#3. Create an inner function to calculate the addition in the following way
#	a. Create an outer function that will accept two parameters, a and b
#	b. Create an inner function inside an outer function that will calculate the addition of a and b
#	c. At last, an outer function will add 5 into addition and return it
def addition(c,d):
    def sum(c,d):
        return c+d
    res = sum(c,d)
    return res+5
outcome = addition(10,10)
print(outcome)

#4. Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
def sum(n):
    if n<=1:
        return n
    return n + sum(n-1)
n=10
print("The sum is :",sum(n))
#5. Assign a different name to function and call it through the new name
def display_student(name, age):
    print(name)
    print(age)
show_student=display_student
show_student("Gishnavi",21)
#6. Find the largest item from a given list without using inbuilt methods
def large(arr):
    maximum = arr[0]
    for num in arr:
        if(num > maximum):
           maximum= num
    return maximum
list = [10,24,55,20,60]
result = large(list)
print("The largest item from a given list:",result)



