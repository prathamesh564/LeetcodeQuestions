class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def trav(node):
            if not node:
                return
            trav(node.left)
            res.append(node.val)
            trav(node.right)
        trav(root)
        return res        
