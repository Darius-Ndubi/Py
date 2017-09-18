#credit card verification via Luhn algorithm
#first we verify visa cards with mod 10 algorithm

#function that verifies visa cards

def visa(card_num):
	#first, starting with the first num, double the odd digits abd sum them up
	i=0
	sum1=0
	while i<len(card_num):
		k=card_num[i]
		g=k*2
		if g>9:
			new_g=g-9
			new_list.append(new_g)
		elif g<9:
			g==g
			new_list.append(g)
		i+=2

#add the newlist and store it aside
	sum1=sum(new_list)
#generate a list of numbers in odd places of  credit card list
	odd_places=card_num[1::2]
	sum2=sum(odd_places)
#sum up the two lists

	sum3=sum1+sum2
	if sum3%10==0:
		print "Your visa card is valid"
	else:
		print "Your card is invalid"
		print "Visit issuerer to sort out the problem!!"

#function that verifies Discover cards
def discover(card_num):
	#picking odd numbers in the sequence starting with index 0
	dis_list=card_num[0::2]
	i=0
	while i<len(dis_list):
		k=dis_list[i]
		g=k*2
		if g>9:
			new_g=g-9
			new_list.append(new_g)
		elif g<9:
			g==g
			new_list.append(g)
		i+=1

#suming the new list of numbers
	sum1=sum(new_list)

#picking the numbers that were not doubled in the credit card number list
	odd_places=card_num[1::2]
	sum2=sum(odd_places)

#suming up the two lists
	sum3=sum1+sum2

	if sum3%10==0:
		print "Your Discovery card is valid"
	else:
		print "Your card is in valid"
		print "Check your provider for assistance..."


#give out the format that will be used by users

print "Enter credit card number in this format 0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5"

card_num=list(input("Enter the credit card number: "))

#create an empty list that will be used to store card number sequence
new_list=[]

def choice():
	print "Which card would you like to verify?"
	print "This program verifies visa,discovery, cards"
	choice_name=raw_input("Enter the card name you would like to verify: ").lower()
	if choice_name[0]=='v':
		visa(card_num)
	elif choice_name[0]=='d':
		discover(card_num)


choice()
