class Queue:
	def __init__(self):
		self.queue = []

	def enqueue(self, data):
		self.queue.insert(0,str(data))

	def dequeue(self):
		self.queue.pop()

	def isempty(self):
		return self.queue == []

	def size(self):
		print(len(self.queue))

	def pprint(self):
		print('\n'.join(self.queue))


if __name__=='__main__':
	q = Queue()
	q.enqueue(10)
	q.enqueue(20)
	q.enqueue(30)
	q.pprint()
	q.dequeue()
	q.pprint()
	q.size()
	print(q.isempty())
