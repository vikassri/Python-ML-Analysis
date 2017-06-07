class Stack:
	def __init__(self):
		self.stack = []

	def push(self, data):
		self.stack.append(str(data))

	def pop(self):
		del self.stack[0]

	def peak(self):
		print(self.stack[-1])

	def isempty(self):
		return self.stack == []

	def size(self):
		print(len(self.stack))

	def pprint(self):
		print('\n'.join(self.stack))


if __name__=='__main__':
	s = Stack()
	s.push(10)
	s.push(20)
	s.push(30)
	s.pprint()
	s.pop()
	s.pprint()
	s.size()
	print(s.isempty())