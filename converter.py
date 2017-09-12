
#volume unit converter from cm^3 to m^3 and back
def conv_volume():
	print "For volume conversion to cm^3 press 'c' and m^3 press 'm'"
	choice=raw_input("Enter your choice: ")
	if choice=='c':
		vol=input("enter your volume value in meters cubic: ")
		result=vol*1000000.0
		print "Your volume is: ",result,"cm cubic"
	elif choice=='m':
		vol=input("Enter your volume in cm cubic: ")
		result=vol/1000000.0
		print "Your volume is: ",result,"meters cubic"
	else:
		print "ERROR...... \n Choice not provide!!"


#mass conversion function
def conv_mass():
	print "For conversion to grams press 'g' and to kgrams press 'k'"
	choice=raw_input("Enter your choice: ")
	if choice=='g':
		mas=input("Enter the value of kgs: ")
		result=mas*1000
		print "Your volume is: ",result,"grams"
	elif choice=='k':
		mas=input("Enter the value of grams: ")
		result=mas/1000.0
		print "Your volume is: ",result,"kilograms"
	else:
		print "ERROR...... \n Choice not provided!!"

#temperature conversion function
def conv_temperature():
	print "To convert to celcius press 'c' and to farenheit press 'f'"
	choice=raw_input("Enter your choice: ")
	if choice=='c':
		temp=input("Enter the temperature in farenheit: ")
		result=((temp-32)*(5.0/9))
		print "Your temperature is: ",result,"Celcius"
	elif choice=='f':
		temp=input("Enter the temperature in Celcius: ")
		result=(((9.0*temp)/5)+32)
		print "Your temperature is : ",result,"Farenheit"
	else:
		print "ERROR..... \n Choice not provided!!"

#currecy conversion function from US-dollas to Kenyan shilling and back
#using exchange rate as of 11th Sept 2017
def conv_currency():
	print "To convert to K-shilings press 'k' and to US-Dollas press 'd'"
	choice=raw_input("Enter your choice: ")
	if choice=='k':
		currency=input("Enter the amount in dollas you want to be converted to shillings: ")
		exchange=currency*102.601
		print "Your amount in k_shillings is: ",exchange
	elif choice=='d':
		currency=input("Enter the amount in kenya shillings: ")
		exchange=currency*0.00974649
		print "Your money in US-Dollas is: ",exchange

#A main function that calls all the other functions to work
def conv_main():
	while True:
		print "The folowing are the conversions that can be done:\n volume \n mass \n currency \n temperature"
		choice=raw_input("what coversion would you make: ").lower()
		if choice[0]=='v':
			conv_volume()
		elif choice[0]=='m':
			conv_mass()
		elif choice.startswith('c')==True:
			conv_currency()
		elif choice.startswith('t')==True:
			conv_temperature()
		else:
			print "ERROR....... \n Retry again!!"


#Calling the main conversion function
conv_main()
