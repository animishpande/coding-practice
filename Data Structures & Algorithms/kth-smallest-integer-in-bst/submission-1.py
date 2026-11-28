# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        sett = set()

        def dfs(curr):
            if not curr:
                return 0
            
            sett.add(curr.val)
            dfs(curr.left)
            dfs(curr.right)
        
        dfs(root)
        print(sett)
        l = list(sett)
        if k > 0:
            return l[k-1]
        return l[k]