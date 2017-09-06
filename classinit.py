#finding area of sphere and volume using classes
class Sphere(object):
	#class object attributes
	pi=3.142
	#class methods
	def __init__ (self,rad=1):
		self.rad=rad
	#method of finding the area
	def area(self):
		#area of sphere
		return (self.rad**2)*Sphere.pi*0.3333
	#Method for calculating the volume
	def vol(self):
		return(self.rad**3)*Sphere.pi*1.3333


d=Sphere(rad=13)

print 'The area is : ',d.area()
print 'The volume is :',d.vol()


