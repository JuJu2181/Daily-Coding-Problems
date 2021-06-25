"""
# Day 8
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""
import json
class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def getUnivalCount(root):
    # if the node is null return the count as 0
    if not root:
        return 0
    # check if it is a leaf node
    if root.left == None and root.right == None:
        return 1
    #if the root node is not empty and also not a leaf node 
    else:
        #firstly find the right and left child unival count recursively
        left_child_count = getUnivalCount(root.left)
        right_child_count = getUnivalCount(root.right)
        total_count = left_child_count + right_child_count 
        # it the left child and right child value is same as root value then increase the total unival count by 1 else keep the count same
        return total_count if root.left and root.left.val != root.val or root.right and root.right.val != root.val else total_count+1

def main():
    node = Node(
        '0',
        Node('1'),
        Node(
            '0',
            Node('1',Node('1'),Node('1')),
            Node('0')
            )
    )
    print(f'Total Unival Tree Count: {getUnivalCount(node)}')

if __name__ == '__main__':
    main()