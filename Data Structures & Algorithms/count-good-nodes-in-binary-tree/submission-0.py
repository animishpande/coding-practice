# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # if not root:
        #     return 0
        # sett = set()

        # def dfs(curr):
        #     if not curr:
        #         return 0
            
        #     if len(sett) >= 1:
        #         print(curr.val)
        #         check = all(curr.val > e for e in sett)
        #         if check:
        #             sett.add(curr.val)
        #     else:
        #         sett.add(curr.val)
        #     left = dfs(curr.left)
        #     right = dfs(curr.right)

        # dfs(root)
        # return len(sett)
        def dfs(node, maxVal):
            if not node:
                return 0
            
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        return dfs(root, root.val)

        