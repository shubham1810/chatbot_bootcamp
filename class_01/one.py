# Functions in Python

"""def myFunction(m, c, *args, **kwargs):

	def add(x):
		return m*x + c

	return add

line1 = myFunction(1.0, 5.0)
line2 = myFunction(0.5, -2.0)

print line2(3), line1(4)"""

def someFunction(key, value, d=None):
	if d is None:
		d = dict()
	d[key] = value
	return d


if __name__ == '__main__':
	
	c1 = someFunction(1, 5)
	c2 = someFunction('a', 0, {})
	c3 = someFunction('k', 'a')
	c4 = someFunction(9, 'a', {'k':0})

	print c1	# {1:5}
	print c2	# {1:5, 'a':0}, {'a':0}
	print c3	# {1:5, 'k':'a'}, {'k':'a'}, {'k':'a', 'a':0}
	print c4	# {9:'a', 'k':0}