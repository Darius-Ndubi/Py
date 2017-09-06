#checking for names in a list of users

user=('Admin','SuperAdmin','Guest','Group')
name=raw_input('Enter your user level clearance: ')
#print name in user
#print ('Login')
if (name in user):print 'Welcome !! ',name
