def addMe(a, b):
	return a + b


def duplicateString(s, i):
	return s*i


class A:
	def __init__(self, k=9):
		self.k = k


class MyClass:
	def __init__(self, x=1, y=2):
		self.x = x
		self.y = y
		self.o = A(10)

	def getValueX(self):
		return self.x

	def getValueY(self):
		return self.y

	def getSum(self):
		return self.x + self.y


if __name__ == '__main__':
	# print addMe(1, 4)
	# print duplicateString('#', 5)
	#a = [MyClass(1, -3), MyClass(-1, 3), MyClass(91, -93), MyClass(-10, 0)]
	#a = sorted(a, key=lambda z: z.x)
	import copy
	#for ix in a:		print ix.x, ix.y
	a = MyClass()
	b = copy.deepcopy(a)
	c = a
	print a
	print b==a
	print c
	