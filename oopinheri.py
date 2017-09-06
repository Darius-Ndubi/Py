#finding the distance and slope in two given cooordinates and line
print "Enter your cooordinates in form of a list eg. [a,b] and [b,c]"
import cmath
coor1=input("Enter your first coordinates in a list as shown above")
coor2=input("Enter your second coordinates in a list as shown above")
class Line(object):
#class methods
	def __init__(self,coor1,coor2):
		self.coor1=coor1
		self.coor2=coor2

	def distance(self):
#woorking out the distance between the two points
		i=coor2[0]-coor1[0]
		j=coor2[1]-coor1[1]
		print "The distance between the two coordinates is: ",pow(((i*1.0)**2)+(j**2),0.5)
#method to calculate the slope between two coordinate points
	def slope(self):
                i=coor2[0]-coor1[0]
                j=coor2[1]-coor1[1]
		k=(j*1.0)/i
		print "The slope between the two points is: ",k


l=Line(coor1,coor2)

l.distance()

l.slope()


#finding the volume of cylinder using classes
height=input("Enter the height of the cylinder: ")
radius=input("Enter the radius of the cylinder: ")
pi=3.14159
class Cylinder(object):
	#class object attributes

	#class methods
	def __init__(self,height,radius):
		self.height=height
		self.radius=radius
	def volume(self):
		print "The volume is: " ,(pi*(self.radius*self.radius*self.height)),"cm^3"
	def surfaceA(self):
		print "the Surface area of the cylinder is: ",(2*(pi*(self.radius**2)))+self.height*pi*2*self.radius,"cm^2"



k=Cylinder(height,radius)

k.volume()

k.surfaceA()
