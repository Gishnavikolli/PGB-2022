#Create a Time class and initialize it with hours and minutes.
#	a. Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
#	b. Make a method displayTime which should print the time.
#	c. Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.
class Time():
	def __init__(self, hours, minutes):
		self.hours = hours
		self.minutes = minutes
	def addTime(t1, t2):
		t3 = Time(0,0)
		if t1.minutes+t2.minutes > 60:
			t3.hours = (t1.minutes+t2.minutes)/60
		t3.hours = t3.hours+t1.hours+t2.hours
		t3.minutes = (t1.minutes+t2.minutes)-(((t1.minutes+t2.minutes)/60)*60)
		return t3
	def displayTime(self):
		print ("Time in hours:",self.hours,"hours")
	def displayMinute(self):
		print ("Time in minutes:",(self.hours*60)+self.minutes)
a = Time(2,50)
b = Time(1,20)
c = Time.addTime(a,b)
b.displayTime()
b.displayMinute()
