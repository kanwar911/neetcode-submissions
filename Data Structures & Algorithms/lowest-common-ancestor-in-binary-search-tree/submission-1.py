# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # both smaller -> left
    # both bigger  -> right
    # otherwise    -> found LCA
        # if root.val > p.val and root.val > q.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
            
        # if root.val < p.val and root.val < q.val:
        #     return self.lowestCommonAncestor(root.right, p, q)

        # return root
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr