#error handling using try and except
try:
	for i in ['a','b','c']:
		print i**2
except:TypeError
print "the items in the list are not integers"

try:
	a=4
	b=0
	c=a/b
except:
	print"Error dividing number by zero"
#will always be run irespective of the error s occuring above
finally:
	print "All Done"

#function that queries user to allways input an interger and only takes an integer and works its square
def square():
	while True:
		try:
			put=int(raw_input("Enter an integer: "))
		except:
			print"Thats not a number!!"
			continue
		else:
			print"Thats an int :)"
			d=put**2
			break
	print "Thank you,your number squared is: ",d

square()

