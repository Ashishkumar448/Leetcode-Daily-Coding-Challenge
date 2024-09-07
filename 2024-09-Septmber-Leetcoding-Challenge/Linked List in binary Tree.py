# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        # Function to check if current node in tree matches the linked list path
        def dfs(head, node):
            if not head:  # Linked list is fully matched
                return True
            if not node:  # Tree path ends, but linked list does not match completely
                return False
            # Check if current node matches the linked list node and continue DFS on both children
            if head.val == node.val:
                return dfs(head.next, node.left) or dfs(head.next, node.right)
            return False

        # Main function to start checking from each node in the tree
        if not root:
            return False
        # Check if the path starts at root, or in left or right subtree
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
