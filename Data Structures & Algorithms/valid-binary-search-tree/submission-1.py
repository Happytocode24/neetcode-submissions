# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# TopDown approach
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # def dfs(node,min_val,max_val):
        #     if node is None:
        #         return True
        #     if node.val<=min_val or node.val>=max_val:
        #         return False
            
        #     left_valid=dfs(node.left,min_val,node.val)
        #     right_valid=dfs(node.right,node.val,max_val)
        #     return left_valid and right_valid 


        # return dfs(root,float('-inf'),float('inf'))

        # Bottom up approach
        def dfs(node):
            if node is None:
                return True, float('inf'), float('-inf')

            left_valid, left_min, left_max = dfs(node.left)
            right_valid, right_min, right_max = dfs(node.right)

            if not left_valid or not right_valid:
                return False, 0, 0

            if node.val <= left_max or node.val >= right_min:
                return False, 0, 0
            min_val = min(left_min, node.val) 
            max_val = max(right_max, node.val)
            return True, min_val, max_val

        is_valid, min_val, max_val = dfs(root)
        return is_valid