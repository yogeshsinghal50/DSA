'''
https://www.techiedelight.com/print-top-view-binary-tree/
Given the root of a binary tree, return the top view of its nodes' values. Assume the left and right child of a node makes a 45–degree angle with the parent.

Input:
		   1
		 /	 \
		/	  \
	   2	   3
	  		 /   \
	 	  	/	  \
		   5	   6
		 /   \
		/	  \
	   7	   8

Output: [2, 1, 3, 6]

Input:

	  1
	/   \
   /	 \
  2		  3
   \
	\
	 4
	  \
	   \
		5

Output: [2, 1, 3]

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
	def getTopView(self,root:Node,dist,level,d):
		if root is None:
			return
		if dist not in d or level < d[dist][1]:
			d[dist] = (root,level)
		self.getTopView(root.left,dist-1,level+1,d)
		self.getTopView(root.right,dist+1,level+1,d)
		
	def findTopView(self, root: Node) -> List[int]:
		d = {}
		self.getTopView(root,0,0,d)
		result = []
		for key in sorted(d.keys()):
			result.append(d[key][0].data)
		return result

