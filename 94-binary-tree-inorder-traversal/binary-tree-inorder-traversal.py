# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, node):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        def inorder(node,result):
            if node is None:
                return 
            inorder(node.left,result)
            result.append(node.val)
            inorder(node.right,result)
        inorder(node,result)
        return result