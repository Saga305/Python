"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

===========TESTINGS====================

Saga@Saga-Inspiron-5520:~$ python3 t.py 
	Enter the list of numbers(use -1 element to verify failed test):[1,2,3,4]
	Test Passed
	seralized data:  [1, -1, 2, -1, 3, -1, 4, -1, -1]
	seralized form of de-seralized data:  [1, -1, 2, -1, 3, -1, 4, -1, -1]

Saga@Saga-Inspiron-5520:~$ python3 t.py 
	Enter the list of numbers(use -1 element to verify failed test):[1,2,3,4,-1]
	Test Failed
	seralized data:  [1, -1, -1, -1, 2, -1, 3, -1, 4, -1, -1]
	seralized form of de-seralized data:  [1, -1, 2, -1, 3, -1, 4, -1, -1]


"""
class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

class Tree:

	def __init__(self):
		self.root = None

	def insert(self, node, data):
		if node == None:
			self.root = Node(data)
		else:
			if data < node.data:
				if node.left == None :
					node.left = Node(data)
				else:
					self.insert(node.left, data)
			else:
				if node.right == None :
					node.right = Node(data)
				else:
					self.insert(node.right, data)
		

def serializer(node,val):
	if node == None :
		val.append(-1)
	else:
		val.append(node.data)
		serializer(node.left,val)
		serializer(node.right,val)

def serialize(root):
	datas = []
	serializer(root,datas)
	return datas

def deserialize(s):
	tree = Tree()
	for i in range(len(s)):
		if s[i] != -1:
			tree.insert(tree.root, s[i])
	return tree.root

if __name__ == '__main__':
	numbers = eval(input("Enter the list of numbers(use -1 element to verify failed test):"))
	tree = Tree()
	for number in numbers:
		tree.insert(tree.root, number)
	serial = serialize(tree.root)
	serofDes = serialize(deserialize(serial))
	if serial == serofDes:
		print("Test Passed")
	else:
		print("Test Failed")
	print("seralized data: ",serial)
	print("seralized form of de-seralized data: ",serofDes)
