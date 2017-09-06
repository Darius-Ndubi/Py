#conputing volume using function in two ways
import cmath
pi=3.142

def vol(rad):

#local variables
	return(4/3.0)*pi*pow(rad,3)

print vol(3)

#or using lambda assignment

vol1=lambda rad:(4/3.0)*pi*pow(rad,3)
v=vol1(4)
print 'The lambda calculated volume is: ',v

#checking if a number is in a given range of values
def chk(num,low,high):
	if num in range(low,high):
		print 'number is within the range'
	else:
		print 'number not within the range'

chk(5,3,6)


#input a string and count numper of upper n lower case characters



#palindrome
e=raw_input('Enter a word: ')
def pali(e):
	if e[:]==e[::-1]:
		print 'Word is palindrome'
	else:
		print'Word not palindrome'

pali(e)

#panagram

#import string
#def pana(srt1,alphabet=string.ascii_lowercase):
#	alphaset=set(alphabet)
#	return alphaset <= set(str1.lower())

#pana('This is a normal sentence')

#multioly through a list
def multi(nums):
	tot=nums[0]
	for i in nums:
		tot=tot*i
	return tot

print multi([1,2,34,4])
