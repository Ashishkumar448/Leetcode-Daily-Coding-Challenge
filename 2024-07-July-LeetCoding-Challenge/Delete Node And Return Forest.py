from typing import List, Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        forest = []

        def helper(node, is_root):
            if not node:
                return None
            root_deleted = node.val in to_delete_set
            if is_root and not root_deleted:
                forest.append(node)
            node.left = helper(node.left, root_deleted)
            node.right = helper(node.right, root_deleted)
            return None if root_deleted else node

        helper(root, True)
        return forest

# Example usage
# Constructing the binary tree: 
#     1
#    / \
#   2   3
#  / \   \
# 4   5   6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

solution = Solution()
to_delete = [3, 5]
forest = solution.delNodes(root, to_delete)

# The forest should contain the following trees:
#     1       6
#    / \
#   2   4
# In the form of a list of TreeNode objects
for tree in forest:
    # Perform any operation you want with the resulting trees
    print(tree.val)
