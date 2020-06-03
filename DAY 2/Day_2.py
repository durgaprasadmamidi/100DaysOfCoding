class Points(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
	
	def __str__(self):
	 	return "("+str(self.x)+","+str(self.y)+")"

	def __add__(self,other):
		return Points(self.x+other.x,self.y+other.y)

	def __len__(self):
		import math
		return math.sqrt(math.pow(self.x,2) + math.pow(self.y,2))

	def distance(self,other):
		import math
		return math.sqrt(math.pow(self.x-other.x,2) + math.pow(self.y-other.y,2))

p1 = Points(1,1)
p2 = Points(3,3)
print(p1)
print(p2)
print(p1+p2)
print(len(p1))
print(p1.distance(Points(0,0)))
print(p1.distance(p2))

