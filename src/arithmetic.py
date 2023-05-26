from typing import Any

class Arithmetic():
	
	#Initialise with inputs
	def __init__(self, a: Any, b: Any):
		self.a = a
		self.b = b
	
	
	#add numbers
	def add(self):
		return self.a + self.b
	
	
	#subtract numbers
	def sub(self):
		return self.a - self.b
	

	def mul(self):
		return self.a * self.b

	
	def divide(self):
		return self.a/self.b

if __name__ == "__main__":
	print("Hello, world!")


