#Write an “abstract” class, Box, and use it to define some methods which any box object should have: 
#	a. add, for adding any number of balls to the box, 
#	b. empty, for taking all the balls out of the box and returning them as a list, and 
#	c. count, for counting the balls which are currently in the box. 
#	d. Write a simple Item class which has a name attribute and a value attribute – you can assume that all the balls you will use will be Item objects. 
class Box:
    def add(self, *balls):
        raise NotImplementedError()
    def empty(self):
        raise NotImplementedError()
    def count(self):
        raise NotImplementedError()
class Ball:
    def __init__(self, name, value):
        self.name = name
        self.value = value
class ListBox(Box):
    def __init__(self):
        self._balls = []
    def add(self, *balls):
        self._balls.extend(balls)
    def empty(self):
        balls = self._balls
        self._balls = []
        return balls
    def count(self):
        return len(self._balls)
class DictBox(Box):
    def __init__(self):
        self._balls = {}

    def add(self, *balls):
        self._balls.update(dict((i.name, i) for i in balls))
    def empty(self):
        balls = list(self._balls.values())
        self._balls = {}
        return balls
    def count(self):
        return len(self._balls)