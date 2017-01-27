# a = input("Enter a Number: ")

# String change using splitting
# lists

#slicing arr[start:(end+1):skip]

# check a[1:4:-1]
# loop in join function

"""
if (a%2 == 0) and (a%3==0):
	print "both"
elif (a%2==0):
	print "Two"
elif (a%3 == 0):
	print "three"
else:
	print "None"
"""

# Loops
i = 1
# FizzBuzz
""" if number divisible by 3: print Fizz
if divisible by 5: print Buzz
if both: print FizzBuzz
else: print number
"""
"""
while True:
	if (i%3==0) and (i%5==0):
		print "FizzBuzz"
	elif not i%3:
		print "Fizz"
	elif not i%5:
		print "Buzz"
	elif i >= 30:
		break
	else:
		print i
	i += 1


i = 0

while True:
	if i%2==0:
		print i
	elif i%3==0:
		i+= 1
		continue
	elif i>=10:
		break
	else:
		pass

	print "Statement", i
	i += 1
"""

# For loops
v = ['a', 1, 4, 3, [11, 3]]
for i in range(len(v)):
	print v[i]

a = [ix**3 for ix in range(10)]
print a

print ['a']*5
