#BST data structure implementaion in python.

""" Create Node class"""
class Node:

	def __init__(self,key):
		self.key = key
		self.right = None
		self.left = None

""" Create a BST class"""
class BST:

	def __init__(self):
		self.root = None

	def __insert(self,node,key):
		if self.root == None:
			self.root = Node(key)
		else:
			if key < node.key:
				if node.left == None:
					node.left = Node(key)
				else:
					self.__insert(node.left, key)
			elif key > node.key:
				if node.right == None:
					node.right = Node(key)
				else:
					self.__insert(node.right,key)
			else:
				print("Key {} is already instered.".format(key))

	def __inorderPrint(self,node):
		if self.root == None:
			print("BST is Empty")
		else:
			if node.left != None:
				self.__inorderPrint(node.left)
			print(node.key, "\t" ,sep="", end="")
			if node.right != None:
				self.__inorderPrint(node.right)

	def __findSmallestKey(self,node):
		if self.root == None:
			return -1000
		else:
			if node.left == None:
				return node.key
			if node.left != None:
				return self.__findSmallestKey(node.left)

	def insert(self,key):
		self.__insert(self.root,key)


	def inorderPrint(self):
		self.__inorderPrint(self.root)


	def findSmallestKey(self):
		return self.__findSmallestKey(self.root)


if __name__=="__main__":
	tree = BST()
	l = [10,5,6,3,4,20,7,8,9,0]
	for i in l:
		tree.insert(i)
	tree.inorderPrint()
	print("\n Smallest node = ",tree.findSmallestKey())
