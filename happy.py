#Fun is programming
#From a movie Star trek in which the character generated a sequence of numbers and perported to haveused them to blast the spaceship from crashing into the sun
#takes input form the user and checks if it is a happy number or not

print "A script to check if a number is a happy number or not"
#take in the number as a string so that we can iterate through it
num=raw_input("Enter the number: ")

sum1=0
sum2=0

for i in num:
	j=int(i)**2 #convert to int and square them up
	sum1+=j
	#convert back to strings
	str_sum1=str(sum1)

print sum1

for e in str_sum1:
	k=int(e)**2
	sum2+=k

print sum2

if sum2==1:
	print "The number is a happy number :) !!"
else:
	print "The number is not a happy number ;( !!"



