#BST data structure implementaion in python.

""" Create Node class"""
class Node:

	def __init__(self,key):
		""" Construct a node """
		self.key = key
		self.right = None
		self.left = None

	def isLeft(self):
		""" Check existance of left node """
		return self.left != None

	def isLeftNone(self):
		""" Check none existance of left node """
		return self.left == None

	def isRight(self):
		""" Check existance of right node """
		return self.right != None

	def isRightNone(self):
		""" Check none existance of right node """
		return self.right == None


""" Create a BST class"""
class BST:

	def __init__(self):
		""" Construct binary tree root node """
		self.root = None

	def __isRoot(self):
		""" Check existance of root node [Private method] """
		return self.root != None

	def __isRootNone(self):
		""" Check none existance of root node [Private method] """
		return self.root == None

	def __insert(self,node,key):
		""" Insert a node [Private method] """
		if self.__isRootNone():
			self.root = Node(key)
		else:
			if key < node.key:
				if node.isLeftNone():
					node.left = Node(key)
				else:
					self.__insert(node.left, key)
			elif key > node.key:
				if node.isRightNone():
					node.right = Node(key)
				else:
					self.__insert(node.right,key)
			else:
				print("Key {} is already instered.".format(key))


	def __inOrderPrint(self,node):
		""" Print inorder traversal [Private method] """
		if self.__isRootNone():
			print("BST is Empty")
		else:
			if node.isLeft():
				self.__inOrderPrint(node.left)
			print(node.key, "\t" , end="")
			if node.isRight():
				self.__inOrderPrint(node.right)

	def __preOrderPrint(self,node):
		""" Print preorder traversal [Private method] """
		if self.__isRootNone():
			print("BST is Empty")
		else:
			print(node.key, "\t" , end="")
			if node.isLeft():
				self.__preOrderPrint(node.left)
			if node.isRight():
				self.__preOrderPrint(node.right)

	def __postOrderPrint(self,node):
		""" Print postorder traversal [Private method] """
		if self.__isRootNone():
			print("BST is Empty")
		else:
			if node.isLeft():
				self.__postOrderPrint(node.left)
			if node.isRight():
				self.__postOrderPrint(node.right)
			print(node.key, "\t" , end="")

	def __reverseOrderPrint(self,node):
		""" Print reverseorder traversal [Private method] """
		if self.__isRootNone():
			print("BST is Empty")
		else:
			if node.isRight():
				self.__postOrderPrint(node.right)
			print(node.key, "\t" , end="")
			if node.isLeft():
				self.__postOrderPrint(node.left)


	def __findSmallestKey(self,node):
		""" Find smallest key in given node [Private method] """
		if self.__isRootNone():
			return -1000
		else:
			if node.isLeftNone():
				return node.key
			if node.isLeft():
				return self.__findSmallestKey(node.left)

	def __removeKey(self,node,key):
		""" Remove given key [Private method] """
		pass

	def insert(self,key):
		""" Insert a node """
		self.__insert(self.root,key)

	def inOrderPrint(self):
		""" Print inorder traversal """
		self.__inOrderPrint(self.root)
		print("")

	def preOrderPrint(self):
		""" Print preorder traversal """
		self.__preOrderPrint(self.root)
		print("")

	def postOrderPrint(self):
		""" Print preorder traversal """
		self.__postOrderPrint(self.root)
		print("")

	def reverseOrderPrint(self):
		""" Print reverseorder traversal """
		self.__reverseOrderPrint(self.root)
		print("")

	def findSmallestKey(self):
		""" Find smallest key in given node """
		return self.__findSmallestKey(self.root)

	def removeKey(self,key):
		""" Remove given key  """
		self.__removeKey(self.root,key)

	def getRootKey(self):
		""" Get root key """
		return self.root.key


if __name__=="__main__":
	tree = BST()
	l = [10,5,6,3,4,20,7,8,9,0,11,12,13,14,15]
	for i in l:
		tree.insert(i)
	tree.inOrderPrint()
	tree.preOrderPrint()
	tree.postOrderPrint()
	tree.reverseOrderPrint()
	print("Smallest node = ",tree.findSmallestKey())
	print("Root key = ",tree.getRootKey())
	tree.removeKey(tree.getRootKey())
	tree.inOrderPrint()
