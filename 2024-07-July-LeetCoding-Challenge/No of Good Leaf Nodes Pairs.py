# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0

        def dfs(node):
            if not node:
                return []

            if not node.left and not node.right:
                return [1]

            left_dists = dfs(node.left)
            right_dists = dfs(node.right)

            for l in left_dists:
                for r in right_dists:
                    if l + r <= distance:
                        self.result += 1

            return [n + 1 for n in left_dists + right_dists if n + 1 < distance]

        dfs(root)
        return self.result
