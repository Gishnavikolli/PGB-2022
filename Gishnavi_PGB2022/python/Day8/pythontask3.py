#Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.) and stop after 20 iterations
class Num:
    def __iter__(self):
        self.x =1
        return self
    def __next__(self):
        if self.x<=20:
            n=self.x
            self.x +=1
            return n
        else:
             raise StopIteration
iterclass = Num()
iter = iter(iterclass)
print("The Iteration starts:")
for n in iter:
    print(n)
