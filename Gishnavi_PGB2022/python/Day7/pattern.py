#11 Write a program to use for loop to print the following reverse number pattern

		# 5 4 3 2 1 
		# 4 3 2 1 
		# 3 2 1 
		# 2 1 
		# 1
for j in range(5,0,-1):
	for i in range (j,0,-1):
		print(i,end= " ")
	print()