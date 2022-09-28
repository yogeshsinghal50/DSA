# https://www.techiedelight.com/find-lowest-common-ancestor-lca-two-nodes-binary-tree/

# A class to store a binary tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Function to check if a given node is present in a binary tree or not
def isNodePresent(root, node):
 
    # base case
    if root is None:
        return False
 
    # if the node is found, return true
    if root == node:
        return True
 
    # return true if a given node is found in the left or right subtree
    return isNodePresent(root.left, node) or isNodePresent(root.right, node)
 
 
# Function to find the lowest common ancestor of given nodes `x` and `y`, where
# both `x` and `y` are present in a binary tree.
# The function returns true if `x` or `y` is found in a subtree rooted at the root.
# `lca` —> stores `LCA(x, y)`
def findlca(root, lca, x, y):
 
    # base case 1: return false if the tree is empty
    if root is None:
        return False, lca
 
    # base case 2: return true if either `x` or `y` is found
    # with lca set to the current node
    if root == x or root == y:
        return True, root
 
    # recursively check if `x` or `y` exists in the left subtree
    left, lca = findlca(root.left, lca, x, y)
 
    # recursively check if `x` or `y` exists in the right subtree
    right, lca = findlca(root.right, lca, x, y)
 
    # if `x` is found in one subtree and `y` is found in the other subtree,
    # update lca to the current node
    if left and right:
        lca = root
 
    # return true if `x` or `y` is found in either left or right subtree
    return (left or right), lca
 
 
# Function to find the lowest common ancestor of nodes `x` and `y`
def findLCA(root, x, y):
 
    # `lca` stores the lowest common ancestor
    lca = None
 
    # call LCA procedure only if both `x` and `y` are present in the tree
    if isNodePresent(root, y) and isNodePresent(root, x):
        lca = findlca(root, lca, x, y)[1]
 
    # if LCA exists, print it
    if lca:
        print('LCA is', lca.data)
    else:
        print('LCA does not exist')
 
 
if __name__ == '__main__':
 
    ''' Construct the following tree
          1
        /   \
       /     \
      2       3
       \     / \
        4   5   6
           / \
          7   8
    '''
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    findLCA(root, root.right.left.left, root.right.right)
    findLCA(root, root.right.left.left, Node(10))
    findLCA(root, root.right.left.left, root.right.left.left)
    findLCA(root, root.right.left.left, root.right.left)
    findLCA(root, root.left, root.right.left)