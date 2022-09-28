# https://www.techiedelight.com/determine-two-nodes-are-cousins/

# A class to store a binary tree node
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
 
# A class to store a binary tree node along with its level and parent information
class NodeInfo:
    def __init__(self, node, level, parent):
        self.node = node
        self.level = level
        self.parent = parent
 
 
# Perform inorder traversal on a given binary tree and update 'x' and 'y'
def updateLevelandParent(root, x, y, parent=None, level=1):
 
    # base case: tree is empty
    if root is None:
        return
 
    # traverse left subtree
    updateLevelandParent(root.left, x, y, root, level + 1)
 
    # if the first element is found, save its level and parent node
    if root == x.node:
        x.level = level
        x.parent = parent
 
    # if the second element is found, save its level and parent node
    if root == y.node:
        y.level = level
        y.parent = parent
 
    # traverse right subtree
    updateLevelandParent(root.right, x, y, root, level + 1)
 
 
# Function to determine if two given nodes are cousins of each other
def checkCousins(root, node1, node2):
 
    # return if the tree is empty
    if root is None:
        return False
 
    level = 1       # level of the root is 1
    parent = None   # parent of the root is None
 
    x = NodeInfo(node1, level, parent)
    y = NodeInfo(node2, level, parent)
 
    # perform inorder traversal on the list and update 'x' and 'y'
    updateLevelandParent(root, x, y)
 
    # return true if 'x' and 'y' are at the same level, but different parent
    return x.level == y.level and x.parent != y.parent
 
 
if __name__ == '__main__':
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
 
    if checkCousins(root, root.left.right,  root.right.left):
        print('Nodes are cousins of each other')
    else:
        print('Nodes are not cousins of each other')