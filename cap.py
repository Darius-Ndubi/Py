#finding PI decimal to the nth digit
from math import pi
from math import e

out="PI to the 5th digit is: %.5f"
print out % pi

out2="e to 5th digit is: %.5f"
print out2 % e

#generating the fibonnacci sequence  to the number entered on keyboard

end=input("Enter the number digits of the Fibbonacci sequence: ")

def fibo(end):
	i=0
	start=0
	next=1
	while i<end:
		start,next=next,next+start
		print start
		i+=1

fibo(end)

#asking the user befor displaying the next prime number
print "Use no to stop the sequence and yes to continue"

def prime(ans):
	print "The list starts with"
	print 2
	print 3
	print 5
	print 7
	for i in range(2,100):
		if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
			ans=raw_input("Do you want the next prime number: ")
			ans=ans.lower()
			if ans.startswith('y')==True:
				print i
			else:
				break

prime ('s')


w=input("Enter the width of the floor: ")
h=input("Enter the height of the floor: ")
cost=input("Enter the cost of tile: ")

class Area(object):
	#class object attributes
	tile_area=30

	#class methods
	def __init__(self,w,h,cost):
		self.w=w
		self.h=h
		self.cost=cost
	#method to find cost od tiling the floor of the house
	def find_cost(self):
		area=w*h

		return  ((area*cost)/Area.tile_area)


d=Area(w,h,cost)

print 'The cost of total cost ot tiling the floor is: ',d.find_cost(), 'Ksh'

#calculating the amount of change given in hundreds,ten,and pennies
t_cost=input ("Enter the cost of goods: ")
money=input ("Enter the money you have handed over: ")

def balance(t_cost,money):
	if money<t_cost:
		bal=t_cost-money
		print 'Please add:',bal,'Ksh to take items'
	elif money==cost:
		bal=money-t_cost
		print 'Your balance is: ',bal,'Ksh take items'
	else:
		bal=money-t_cost
                str_bal=str(bal)
                bal_len=len(str_bal)
                if bal_len==4:
                        print 'Amount in thousands is: ', (int(str_bal[0])*1000)
			print 'Amount in hundreds is: ', (int(str_bal[1])*100)
			print 'Amount in tens is: ', (int(str_bal[2])*10)
			print 'Amount in ones is: ', (int(str_bal[3])*1)

                elif bal_len==3:
			print 'Amount in hundreds is: ', (int(str_bal[0])*100)
			print 'Amount in tens is: ', (int(str_bal[1])*10)
			print 'Amount in ones is: ', (int(str_bal[2])*1)


		elif bal_len==2:
			print 'Amount in tens is: ', (int(str_bal[0])*10)
			print 'Amount in ones is: ', (int(str_bal[1])*1)


		elif bal_len==1:
			print 'Amount in ones is: ', (int(str_bal[0])*1)


		print 'Your balance is: ',bal,'Ksh'

balance(t_cost,money)
