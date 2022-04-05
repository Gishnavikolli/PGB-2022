#Write a Python class to find the three elements that sum to zero from a set of n real numbers. 
#	Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
#	Output : [[-10, 2, 8], [-7, -3, 10]]
class elements:
 def Sum(self, numbers):
        l = []
        n=len(numbers)
        for i in range(0, n-2):      
            for j in range(i+1, n-1):           
                for k in range(j+1, n):              
                    if (numbers[i] + numbers[j] + numbers[k] == 0): 
                        l.append([numbers[i], numbers[j], numbers[k]]) 
        return l          
print(elements().Sum([-25, -10, -7, -3, 2, 4, 8, 10]))
 