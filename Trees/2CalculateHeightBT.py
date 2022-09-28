'''
https://www.techiedelight.com/calculate-height-binary-tree-iterative-recursive/
Given the root of a binary tree, return the binary tree's height. The height of the binary tree is the total number of edges or nodes on the longest path from the root node to the leaf node.

The solution should consider the total number of nodes in the longest path. For example, an empty tree's height is 0, and the tree's height with only one node is 1.

Input:
		   1
		 /   \
		/	  \
	   2	   3
	  /	\	  / \
	 /	 \ 	 /	 \
	4	  5	6	  7

Output: 3


Input:
		   1
		  /
		 /
		2
	   /
	  /
	 3
	/
   /
  4

Output: 4

'''
from collections import deque
class Solution:

	'''
	A binary tree node is defined as:

	class Node:
		def __init__(self, data=None, left=None, right=None):
			self.data = data	# data field
			self.left = left	# pointer to the left child
			self.right = right	# pointer to the right child
	'''

	def findHeight2(self, root: Node) -> int:
		if root is None:
			return 0
		return 1 + max(self.findHeight(root.left),self.findHeight(root.right))
	
	def findHeight(self, root: Node) -> int:
		if root is None:
        	return 0
	    # create an empty queue and enqueue the root node
	    queue = deque()
	    queue.append(root)
	 
	    height = 0
	 
	    # loop till queue is empty
	    while queue:
	 
	        # calculate the total number of nodes at the current level
	        size = len(queue)
	 
	        # process each node of the current level and enqueue their
	        # non-empty left and right child
	        while size > 0:
	            front = queue.popleft()
	 
	            if front.left:
	                queue.append(front.left)
	 
	            if front.right:
	                queue.append(front.right)
	 
	            size = size - 1
	 
	        # increment height by 1 for each level
	        height = height + 1
	 
	    return height
