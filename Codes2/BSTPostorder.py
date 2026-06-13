class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def trav(node):
            if not node:
                return
            trav(node.left)
            trav(node.right)
            res.append(node.val)
        trav(root)
        return res        
