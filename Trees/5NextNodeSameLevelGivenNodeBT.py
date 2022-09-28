'''
https://www.techiedelight.com/find-next-node-in-same-level-binary-tree/
Given the root of a binary tree and a tree node x, return the next node at the same level as the node x.

For example, consider the following binary tree.

		   1
		 /   \
		/	  \
	   2	   3
	  / \		\
	 /	 \		 \
	4	  5		  6
				 / \
				/   \
			   7	 8

Input: Node 2
Output: Node 3
Explanation: The next node of 2 is node 3

Input: Node 5
Output: Node 6
Explanation: The next node of 5 is node 6

Input: Node 8
Output: None
Explanation: The next node of 8 doesn't exist.

Note: The solution should return None if x is not the actual tree node.

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
	def findNode(self,root,node,level,node_level):
		if root is None:
			return None, node_level
		if root is node:
			return None, level
		elif node_level and level == node_level:
			return root,level
		left, node_level = self.findNode(root.left,node,level+1,node_level)
		if left:
			return left, node_level
		return self.findNode(root.right,node,level+1,node_level)
		
	def findNextNode(self, root: Node, x: Node, ) -> Node:
		return self.findNode(root,x,level=1,node_level=0)[0]

