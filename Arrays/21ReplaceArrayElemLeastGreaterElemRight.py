
# https://www.techiedelight.com/replace-every-element-array-least-greater-element-right/

# A class to store a BST node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
 
# Function to insert a specified key into the binary search tree
# rooted at the specified node and find its successor
def insert(root, key, successor):
 
    # base case: empty tree
    if root is None:
        return Node(key), successor
 
    # if the key is less than root
    if key < root.key:
 
        # set successor as the current node
        successor = root.key
 
        # traverse the left subtree
        root.left, successor = insert(root.left, key, successor)
 
    # if the key is more than root
    elif key > root.key:
 
        # traverse the right subtree
        root.right, successor = insert(root.right, key, successor)
 
    return root, successor
 
 
# Replace each element of the specified list with the
# least greater element on its right
def replace(nums):
 
    # root of the binary search tree
    root = None
 
    # traverse the list from the end
    for i in reversed(range(len(nums))):
        # insert the current element into the binary search tree
        # and replace it with its inorder successor
        successor = -1
        root, successor = insert(root, nums[i], successor)
        nums[i] = successor
 
    # print the resultant list
    print(nums)
 
 
if __name__ == '__main__':
 
    nums = [10, 100, 93, 32, 35, 65, 80, 90, 94, 6]
 
    replace(nums)