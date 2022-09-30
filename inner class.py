'''
Class inside class
-> we define one class inside another class
-> Make object of inner class in inside outer class
'''

class student:

	def __init__(self,name,roll): #outer class
		self.name = name
		self.roll = roll
		self.lap = self.laptop() #object of inner class

	def show(self):
		print(self.name,self.roll)
		self.lap.show()

	class laptop: #inner class
		def __init__(self):
			self.brand = 'Lenovo'
			self.cpu = 'i5 7th gen'
			self.ram = 16

		def show(self):
			print(self.brand,self.cpu,self.ram)

s1 = student('Harsh',27)
s2 = student('Python',22)

s1.show()

print(s1.lap.cpu)

# lap1 = student.laptop() #object making outside class

lap1 = s1.lap
lap2 = s2.lap

print(id(lap1))
print(id(lap2))