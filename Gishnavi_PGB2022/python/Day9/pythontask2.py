#2. Design simple calculater application where user input is assumed to be a formula that consist of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:

#	a. If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
#	b. Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError
#	c. If the second input is not '+' or '-', again raise a FormulaError
#	d. If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, until the user enters quit.
def calculate(num1, op, num2):
  if op == '+':
    return num1 + num2
  if op == '-':
    return num1 - num2
  if op == '*':
    return num1 * num2
  if op == '/':
    return num1 / num2
  raise FormulaError('{} is not a valid operator'.format(op))
class FormulaError(Exception):
     pass
def user_input(user):
  input_list = user.split()
  if len(input_list) != 3:
    raise FormulaError('Input does not consist of three elements')
  n1, op, n2 = input_list
  try:
    n1 = float(n1)
    n2 = float(n2)
  except ValueError:
    raise FormulaError('The first and third input value must be numbers')
  return n1, op, n2
while True:
  user = input('>>> ')
  if user == 'quit':
    break
  try:
      n1, op, n2 = user_input(user)
      res = calculate(n1, op, n2)
      print(res)
  except Exception as e:
      print(e)
