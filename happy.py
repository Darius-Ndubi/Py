#Fun is programming
#From a movie Star trek in which the character generated a sequence of numbers and perported to haveused them to blast the spaceship from crashing into the sun
#takes input form the user and checks if it is a happy number or not

print "A script to check if a number is a happy number or not"
#take in the number as a string so that we can iterate through it
num=raw_input("Enter the number: ")

sum1=0
sum2=0
sum3=0
#function to carry out the first sum
for i in num:
	j=int(i)**2
#	print j
	sum1+=j
	#convert back to strings
	str_sum1=str(sum1)
print str_sum1
if sum1==10:
	print "Your number", num,"is a happy number"

elif sum<>1:
	g=0
	for k in str_sum1:
		h=int(k)**2
#		print h
		sum2+=h
		print sum2
		if sum2==1:
			print "The number",num, "ia a happy number"
	print sum2
	str_sum2=str(sum2)
	if sum2<>1:
		for a in str_sum2:
#okay			print a
			b=int(a)**2
#okay			print b
			sum3+=b
		print sum3
		if sum3==10:
				print "private number"
