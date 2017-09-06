#slicing some part of what was entered by user to display the needed 
#address only

addr=raw_input('Enter your postal code: ')
code= addr[6:18:1] 
#slicing with a step of one

print('your postal code is:'),code

