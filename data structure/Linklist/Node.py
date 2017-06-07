class Node:
	
	def __init__(self, data=None):
		self.data = data
		self.prev = None
		self.next = None

	def set_data(self, data):
		self.data = data

	def set_next(self, data):
		self.next = data

	def set_prev(self, data):
		self.prev = data

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def get_prev(self):
		return self.prev

	def has_next(self):
		return self.next != None
