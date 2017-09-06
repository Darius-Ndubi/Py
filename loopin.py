#the while loop structure with break n continue

a=0
while a<10:
	print 'This is a:',a
	a=a+1

	if a==7:
		print'its seven'
		#break
#with break the loop stops here
	else:
		print 'Continuing....'
		continue

a=0
print a

l=[]

for letter in 'word':
	l.append(letter)

print l

#lis comprehension

l=[l for l in 'word']
print l

#odd numbers list comprehension
o=[]

for add in range (13):
	if add % 2 <> 0:
		o.append(add)

print o

o=[odd for odd in range(15) if odd%2<>0]

print o
