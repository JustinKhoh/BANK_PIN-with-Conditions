# Your pin must fulfil the following requirements
# 1) Each pin should have 6 digits
# 2) No repition of a number 3 times in a row e.g. "111" or "222" etc.
# 3) No 3 consequetive numbers "123" or "234" etc 
# This is my attempt at trying to enforce said requirements on a fake pin

# What is your pin?
PIN = 149544

# Setting up parameters
pin = str(PIN)
numlist = ["0","1","2","3","4","5","6","7","8","9"]
cond2 = []
cond3 = []

##############################################
# Condition 1: Each pin should have 6 digits #
##############################################
if len(pin) < 6:
	print("You pin number has less than 6 digits, please try again")
	exit()
elif len(pin) > 6:
	print("Your pin number has more than 6 digits, please try again")
	exit()

#########################################################
# Condition 2: No repition of a number 3 times in a row #
#########################################################

# Setting up cond2 
# == list of strings with repetition of number 3 times in a row
for i in range(0, len(numlist)):
	cond2_string = ""
	for f in range (0,3):
		cond2_string += numlist[i]
	cond2.append(cond2_string)

# Comparing values in cond2 to pin
for i in range(0,10):
	if cond2[i] in pin:
		print("Your pin has a repition of a number 3 times in a row, please try again")
		exit()

##########################################
# Condition 3: No 3 consequetive numbers #
##########################################

# Setting up cond3
# == list of strings with 3 consecutive numbers
for i in range(0, len(numlist)):
	numstring = ""
	for n in range (0,3):
		try:
			a = str(numlist[i+n])
			numstring += a
		except IndexError:
			numstring = ""
			break
	if len(numstring) == 3:
		cond3.append(numstring)

# Comparing values in cond3 to pin
for i in range(0, len(cond3)):
	if cond3[i] in pin:
		print("Your pin has at least 3 consequetive values in it, please try again")
		exit()

####################################
# If pin fulfils all 3 criteria... #
####################################
print("Your pin is valid")
