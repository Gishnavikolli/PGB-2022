#Write a Python class to get all possible unique subsets from a set of distinct integers. 
#	Input : [4, 5, 6]
#	Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

class set:
    def sub_set(self, s1):
        return self.s2([], sorted(s1))   
    def s2(self, curr, s1):
        if s1:
            return self.s2(curr, s1[1:]) + self.s2(curr + [s1[0]], s1[1:])
        return [curr]
print("The current set is:",set().sub_set([8,7,6]))      
