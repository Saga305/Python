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
			print("BST is Empty ")
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


	def __findSmallestKeyNode(self,node):
		""" Find smallest key in given node [Private method] """
		if self.__isRootNone():
			return -1000
		else:
			if node.isLeftNone():
				return node
			if node.isLeft():
				return self.__findSmallestKeyNode(node.left)

	def __removeKey(self,node,key):
		""" Remove given key [Private method] """
		if self.__isRootNone():
			return self.root
		else:
			if node == None:
				return None
			if key < node.key:
				node.left = self.__removeKey(node.left,key)
			elif key > node.key:
				node.right = self.__removeKey(node.right,key)
			else:

				if node.isLeftNone():
					temp = node.right
					node = None
					return temp
				elif node.isRightNone():
					temp = node.left
					node = None
					return temp

				temp = self.__findSmallestKeyNode(node.right)
				node.key = temp.key
				node.right = self.__removeKey(node.right,node.key)
			return node

	def __getHeight(self,node):
		"""Get Height of the tree """
		if node == None:
			return 0
		hightOfLeftSubTree = self.__getHeight(node.left)
		hightOfRightSubTree = self.__getHeight(node.right)
		return max(hightOfLeftSubTree,hightOfRightSubTree) + 1

	def __getBalanceFactor(self,node):
		"""Get Balance Factor of given node """
		if node == None:
			return -10000
		hightOfLeftSubTree = self.__getHeight(node.left)
		hightOfRightSubTree = self.__getHeight(node.right)
		return hightOfLeftSubTree - hightOfRightSubTree

	def __display(self,node,level):
		"""Print tree """
		if node != None:
			self.__display(node.right,level + 1)
			print("")
			if node == self.root:
				print("Root ->",end="")
			if node != self.root:
				for i in range(level+1):
					print("    ",end= "")
			print(node.key, end="")
			self.__display(node.left,level+1)

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
		return self.__findSmallestKeyNode(self.root).key

	def removeKey(self,key):
		""" Remove given key  """
		self.root = self.__removeKey(self.root,key)

	def getRootKey(self):
		""" Get root key """
		return self.root.key

	def getHeight(self):
		"""Get Height of the tree """
		return self.__getHeight(self.root)

	def getBalanceFactor(self):
		"""Get Balance Factor of root node """
		return self.__getBalanceFactor(self.root)

	def display(self):
		"""Print tree """
		self.__display(self.root,1)
		print("")


if __name__=="__main__":
	tree = BST()
	l = [10,5,4,15,12]
	for i in l:
		tree.insert(i)
	tree.inOrderPrint()
	print("Height of the tree : ",tree.getHeight())
	print("Balance Factor of the tree : ",tree.getBalanceFactor())
	tree.display()
	key = int(input("Enter a key you want to delete(Enter -1 to Exit):"))
	while key != -1:
		tree.removeKey(key)
		tree.inOrderPrint()
		key = int(input("Enter a key you want to delete(Enter -1 to Exit):"))
