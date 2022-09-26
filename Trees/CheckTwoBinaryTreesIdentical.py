'''
https://www.techiedelight.com/check-if-two-binary-trees-are-identical-not-iterative-recursive/
Given the root of two binary trees, x and y, check if x is identical to y. Two binary trees are identical if they have identical structure and their contents are also the same.

Input:
		   1						1
		 /   \					  /   \
		/	  \					 /	   \
	   2	   3				2		3
	  /	\	  / \			   / \	   / \
	 /	 \ 	 /	 \			  /	  \	  /	  \
	4	  5	6	  7			 4	   5 6	   7

Output: True
Explanation: Both binary trees have the same structure and contents.

Input:
		   1						1
		 /   \					  /   \
		/	  \					 /	   \
	   2	   3				2		3
	  /	\	  / \			   / \	   /
	 /	 \ 	 /	 \			  /	  \	  /
	4	  5	6	  7			 4	   5 6

Output: False
Explanation: Both binary trees have different structures.

Input:
		   1						1
		 /   \					  /   \
		/	  \					 /	   \
	   2	   3				2		3
	  /	\	  / \			   / \	   / \
	 /	 \ 	 /	 \			  /	  \	  /	  \
	4	  5	6	  7			 4	   5 6	   8

Output: False
Explanation: Both binary trees have the same structure but differ in nodes' values.

'''

class Solution:

	'''
	A binary tree node is defined as:

	class Node:
		def __init__(self, data=None, left=None, right=None):
			self.data = data	# data field
			self.left = left	# pointer to the left child
			self.right = right	# pointer to the right child
	'''

	def isIdentical(self, x: Node, y: Node) -> bool:
		if x is None and y is None:
			return True
		if x is None:
			return False
		if y is None:
			return False
		return (x.data == y.data) and self.isIdentical(x.left, y.left) and self.isIdentical(x.right, y.right)

