#pro gram to spell out number in English
#the user enters a number and its spelt out with its suffix in English


def asknum():
	global num
	while True:
		try:
			num=input("Enter a number:")
		except:
			print "Thats not a number!! :("
			continue
		else:
			break


def spell_out(num):
	if num==1:
		str_num=str(num)
		store_num=str_num+"st"
		print "It's spelt out as: ",store_num
	elif num==2:
		str_num=str(num)
		store_num=str_num+"nd"
		print"It's spelt out as: ",store_num
	elif num==3:
		str_num=str(num)
		store_num=str_num+"rd"
		print"It's spelt out as: ",store_num
	elif num>=4 and num<21:
		str_num=str(num)
		store_num=str_num+"th"
		print"It's spelt out as: ",store_num
	elif num>20:
		str_num=str(num)
		len_num=len(str_num)
		if int(str_num[len_num-1])==1:
			store_num=str_num+"st"
			print "It's spelt out as: ",store_num
		elif int(str_num[len_num-1])==2:
			store_num=str_num+"nd"
			print "It's spelt out as: ",store_num
		elif int(str_num[len_num-1])==3:
			store_num=str_num+"rd"
			print "It's spelt out as: ",store_num
		else:
			store_num=str_num+"th"
			print "It's spelt out as: ",store_num

asknum()
spell_out(num)

