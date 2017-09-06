#a generator that generates the squares of numbers up to some number N
num=0
def squares(n):
	for i in range(n):
		yield i**2
num=int(input("Enter a number: "))
for i in squares(num):
	print i


#using a generator to produce random numbers (n)

import random

def randnums(low,high,n):
	i=0
	outlist=[]
	while(i<=n):
		t=random.randint(low,high)
		outlist=t
		yield outlist
		i+=1

low=input("Enter the lower number of the range: ")
high=input("Enter the higher number of the range: ")
n=input("Enter the number of times random numbers should be displayed: ")


for num in randnums(low,high,n):
	print num

#how to use the iter built in function to iterate though a string

g=raw_input("Enter a string \n")
def iteration(g):
	l=len(g)
	i=0
	for i in range(l):
		g=iter(g)
		print next(g)

iteration(g)
