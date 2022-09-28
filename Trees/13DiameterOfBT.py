# https://www.techiedelight.com/find-diameter-of-a-binary-tree/

# A class to store a binary tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Function to find the diameter of the binary tree. Note that the function
# returns the height of the subtree rooted at a given node and the diameter.
def getDiameter(root, diameter):
 
    # base case: tree is empty
    if root is None:
        return 0, diameter
 
    # get heights of left and right subtrees
    left_height, diameter = getDiameter(root.left, diameter)
    right_height, diameter = getDiameter(root.right, diameter)
 
    # calculate diameter "through" the current node
    max_diameter = left_height + right_height + 1
 
    # update maximum diameter (note that diameter "excluding" the current
    # node in the subtree rooted at the current node is already updated
    # since we are doing postorder traversal)
    diameter = max(diameter, max_diameter)
 
    # it is important to return the height of the subtree rooted at the current node
    return max(left_height, right_height) + 1, diameter
 
 
def getBTDiameter(root):
 
    diameter = 0
    return getDiameter(root, diameter)[1]
 
 
if __name__ == '__main__':
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    print('The diameter of the tree is', getBTDiameter(root))