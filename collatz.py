num=input("Enter a number: ")
number=0
collatzNum=[]
while num<>1:
	if num%2==0:
		number=num/2
		collatzNum.append(number)
		num=number
	else:
		number=(num*3)+1
		collatzNum.append(number)
		num=number


print collatzNum

