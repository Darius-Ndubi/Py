#inheriting from the base class to derived class
#Base class

class Houses(object):
	#methods
	def __init__(self):
		print "We have what you want"
	def price(self):
		print "Quote your price!"
	def loca(self):
		print "Within Nairobi"

#derived class

class Manyatta(Houses):
	def __init__ (self):
		Houses.__init__(self)
		print "House created"
	#overide attibuted of method pice from the Base class
	def price(self):
		print "Your cheapest"

s=Manyatta()
#checking if price is overitten in the derived class
s.price()
#checking if location has been inherited
s.loca()

#Special Methods

class Movies(object):
	#class object attributes

	#class methods
	def __init__ (self,Title,Gener,Duration):
		self.Title=Title
		self.Gener=Gener
		self.Duration=Duration

	#to allow printing out  __str__ is used as otherwise only memory is printed out
	def __str__ (self):
		return "Title: %s,Gener: %s, The Duration: %s " %(self.Title,self.Gener,self.Duration)
	def __del__(self):
		print " Movie information is deleted"
m=Movies('The Conjuring 2','Horror','2 hrs')

#this will print out the whole info
m.Title

print m

del m
#checking if deletion is done!

m.Duration


