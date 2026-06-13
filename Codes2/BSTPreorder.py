class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res =[]
        def trav(node):
            if not node:
                return
            res.append(node.val)    
            trav(node.left)
            trav(node.right) 
        trav(root)
        return res       
