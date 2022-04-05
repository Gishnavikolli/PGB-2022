# Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
#	Note: Do not use the same element twice.
#	Input: numbers= [10,20,10,40,50,60,70], target=50
#	Output: 3, 4
class elements:
  def Sum(self, numbers, target):
       dict = {}
       for i, num in enumerate(numbers):
           if target - num in dict:
               return (dict[target - num], i )
           dict[num] = i
print("first index = %d, second index = %d" % elements().Sum((10,20,10,40,50,60,70),50))


