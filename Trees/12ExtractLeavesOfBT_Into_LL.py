'''
https://www.techiedelight.com/extract-leaves-of-binary-tree-into-doubly-linked-list/
Given the root of a binary tree, extract all its leaves into a doubly-linked list, i.e., remove all leaf nodes from the binary tree and construct a doubly linked list out of them.

The solution should process the left child before its right child for each tree node. The extraction should be by rearranging the pointers of the binary tree such that the left pointer should act as the previous pointer, and the right pointer should serve as the next pointer for the doubly linked list node.

Input:

			 1
		   /   \
		 /		 \
		2		  3
	   / \		 / \
	  /	  \		/	\
	 4	   5   6	 7
	/ \		  / \
   /   \	 /   \
  8		9	10	 11

Output:

			 1
		   /   \
		 /		 \
		2		  3
	   /		 /
	  /			/
	 4		   6

8 ⇔ 9 ⇔ 5 ⇔ 10 ⇔ 11 ⇔ 7

The solution should return the head of the doubly-linked list and detach the tree from all its leaf nodes. Assume that the binary tree contains at least two nodes.

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

	def extractLeavesH(self, root: Node,head = None) -> (Node,Node):
		if root is None:
			return None, head
		if root.left is None and root.right is None:
			if head:
				head.left = root
				root.right = head
			head = root
			return None, head
		root.right, head = self.extractLeavesH(root.right,head)	
		root.left, head = self.extractLeavesH(root.left,head)
		return root, head
	
	def extractLeaves(self, root: Node) -> Node:
		return self.extractLeavesH(root)[1]

