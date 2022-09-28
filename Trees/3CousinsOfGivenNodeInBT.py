# https://www.techiedelight.com/print-cousins-of-given-node-binary-tree/

# A class to store a binary tree node
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
 
# Function to find the level of the given node `x`
def findLevel(root, x, index=1, level=0):
 
    # return if the tree is empty or level is already found
    if root is None or level != 0:
        return level
 
    # if the given node is found, update its level
    if root == x:
        level = index
 
    # recur for the left and right subtree
    level = findLevel(root.left, x, index + 1, level)
    level = findLevel(root.right, x, index + 1, level)
 
    return level
 
 
def printLevel(root, node, level):
 
    # base case
    if root is None:
        return
 
    # print cousins
    if level == 1:
        print(root.key, end=' ')
        return
 
    # recur for the left and right subtree if the given node
    # is not a child of the root
    if (not (root.left is not None and root.left == node or
            root.right is not None and root.right == node)):
        printLevel(root.left, node, level - 1)
        printLevel(root.right, node, level - 1)
 
 
# Function to print all cousins of a given node
def printAllCousins(root, node):
 
    # base case
    if not root or root == node:
        return
 
    # find the level of the given node
    level = findLevel(root, node)
 
    # print all cousins of the given node using its level number
    printLevel(root, node, level)
 
 
if __name__ == '__main__':
 
    ''' Construct the following tree
             1
           /   \
          2     3
         / \   / \
        4   5 6   7
    '''
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
 
    printAllCousins(root, root.right.left)