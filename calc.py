# a python program that does most mathematical problems

"""first calculation is done by startting with basic operations like
+,-,/,*,and %. Then later add more complex functionality."""
import math

num1=input("Enter your first number: ")
num2=input("Enter your second number: ")
sign=raw_input("Enter the operation: ")
fact=input("Enter the factorial that you want: ")

def simcalc(num1,num2,sign):
	if sign=='+':
		print 'Your answer of %d %s %d is:'%(num1, sign, num2),num1+num2
	elif sign=='-':
		print 'Your answer of %d %s %d is:'%(num1,sign,num2),num1-num2
	elif sign=='/':
		print 'Your answer of %d %s %d is:'%(num1,sign,num2),num1/(num2*1.0)
	else:
		print 'Your answer of %d %s %d is:'%(num1,sign,num2),num1%num2


simcalc(num1,num2,sign)

fact=range(1,fact+1)

#to find the factorial i used the reduce function that applied the funcion below to 
#the range generated to find the factorial

def factorial(num1,num2):
	return num1*num2


print 'Your factorial is: ', reduce(factorial,fact)


#finding the cosine sine and tangent of numbers
#used inbuilt mudules in math standard library

cst=raw_input("To find cos,tan,sin enter the whole query as cox(x): ").lower()

def sohcahtoa(cst):
	if cst[0]=='c':
		print 'your cosine is: ',math.cos(int (cst[4:6]))
	elif cst[0]=='s':
		print 'Your sine is: ',math.sin(int (cst[4:6]))
	elif cst[0]=='t':
		print 'Your tangent is: ',math.tan(int (cst[4:6]))



sohcahtoa(cst)
