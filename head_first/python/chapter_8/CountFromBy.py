class CountFromBy:
	
	def __init__(self, v:int=0, i:int=1) -> None:
		self.val = v
		self.incr = i

	def increase(self) -> None:
		self.val += self.incr

	def __repr__(self) -> None:
		return str(self.val)


a = CountFromBy() # Object Instantiation
print(a)
a.increase()
print(a)
b = CountFromBy(100, 10)
print(b)
b.increase()
print(b)
c = CountFromBy(i=15)
print(c)
c.increase()
c.increase()
c.increase()
print(c)