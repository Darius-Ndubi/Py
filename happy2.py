num=raw_input("Enter a number: ")

sum1=0

for i in num:
	j=int(i)**2
	sum1+=j
if sum1==1:
	print "Number is a hapy  number: "
else:
	while sum1<>1:
		str_sum1=str(sum1)
		k=sum(int(h)**2 for h in str_sum1)
		if k==1:
			print "Number is a happy number"

