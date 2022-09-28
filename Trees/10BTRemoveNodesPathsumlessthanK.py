'''
https://www.techiedelight.com/truncate-given-binary-tree-remove-nodes-lie-path-sum-less-k/
Given the root of a binary tree and a positive number k, remove nodes from the tree which lie on a complete path having a sum less than k. Since a node can be part of multiple paths, delete it only if all paths from it have a sum less than k.

A complete path in a binary tree is defined as a path from the root to a leaf. The sum of all nodes on that path is defined as the sum of that path.


Input: Below binary tree, k = 20

		 6
	   /   \
	  /		\
	 3		 8
		   /   \
		  /		\
		 4		 2
	   /   \	  \
	  /		\	   \
	 1		 7		3

Output:

	  6
	   \
		\
		 8
		/
	   /
	  4
	   \
		\
		 7

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

	def truncate(self, root: Node, k: int, target: int = 0) -> Node:
		if root is None:
			return None
		target += root.data
		root.left = self.truncate(root.left, k, target)
		root.right = self.truncate(root.right, k, target)
		
		if target < k and (root.left is None and root.right is None):
			return None
		return root

