from Node import *

class singleLinkList:

	length = 0
	
	def __init__(self, head = None):
		self.head = head

	def addfront(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else :
			new_node.set_next(self.head)
			self.head = new_node
		self.length  += 1

	def addLast(self, data):
		new_node = Node(data)
		curr = self.head
		while curr.has_next():
			curr = curr.get_next()
		curr.set_next(new_node)
		self.length  += 1

	def addAtPos(self, data, pos):
		curr = self.head
		new_node = Node(data)
		if pos > self.length :
			print("Position cannot be greater then the length of linklist, adding at last position")
			self.addLast(data)
		elif pos < 0:
			print("Position cannot be less then the Zero, adding at first position")
			self.addfirst(data)
		else :
			for i in range(pos-2):
					curr = curr.get_next()
			temp = curr.get_next()
			curr.set_next(new_node)
			new_node.set_next(temp)
		self.length += 1

	def pprint(self):
		curr = self.head
		lst = []
		for i in range(self.length):
			lst.append(str(curr.get_data()))
			curr = curr.get_next()
		print(' => '.join(lst))

	def size(self):
		print(self.length)

	def searchByIndex(self, index):
		curr = self.head
		counter = 1
		while curr:
			if counter == index:
				print("%i found at index %i" %(curr.get_data(),index))
				return 0
			else :
				curr = curr.get_next()
				counter += 1

	def searchByValue(self, data):
		curr = self.head
		counter = 1
		while curr:
			if curr.get_data() == data:
				print("%i found at index %i" %(curr.get_data(),counter))
				return 0
			else :
				curr = curr.get_next()
				counter += 1

	def printBackward(self):
		curr = self.head
		lst = []
		while curr:
			lst.append(str(curr.get_data()))
			curr = curr.get_next()
		print(' => '.join(lst[::-1]))

	def pop(self):
		curr = self.head
		if self.head == None:
			print("LinkList is already Empty !!!")
		else :
			curr = curr.get_next()
			self.head = curr
			self.length -= 1

	def popLast(self):
		curr = self.head
		while curr.has_next():
			curr = curr.get_next()
		curr.set_next(None)
		self.length -= 1

	def removeAtPos(self, pos):
		curr = self.head
		if pos > self.length and pos < 0:
			print("Position cannot be greaterthen the length of linklist and less than zero")
		elif pos == self.length:
			self.popLast()
		elif pos == 0 :
			self.pop()
		else :
			for i in range(1,pos+1):
				temp = curr
				curr = curr.get_next()
			dele = curr.get_next()
			temp.set_next(dele)
		self.length -= 1


if __name__=='__main__':
	s = singleLinkList()
	s.addfront(10)
	s.addfront(20)
	s.addfront(50)
	s.addfront(60)
	s.addLast(30)
	s.pprint()
	s.size()
	s.searchByIndex(2)
	s.searchByValue(10)
	s.printBackward()
	s.addAtPos(40,3)
	s.pprint()
	s.pop()
	s.popLast()
	s.pprint()
	s.removeAtPos(1)
	s.pprint()


