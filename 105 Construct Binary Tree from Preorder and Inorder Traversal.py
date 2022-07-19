class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        length = len(preorder)
        
        if length < 1:
            return None
        if length == 1:
            return TreeNode(preorder[0])
        
        def build(lin, rin, lpre, rpre):
            root = TreeNode(preorder[lpre])
            
            lin1 = lin
            rin1 = dic_in[root.val]-1
            
            lpre1 = lpre+1
            rpre1 = lpre1+rin1-lin1
            
            lin2 = dic_in[root.val] +1
            rin2 = rin
            
            lpre2 = rpre1+1
            rpre2 = rpre
            
            if lin1 <= rin1:
                root.left = build(lin1, rin1, lpre1, rpre1)
            if lin2 <= rin2:
                root.right = build(lin2, rin2, lpre2, rpre2)
            
            return root
            
            
            
        
        
        
        
        
        
        dic_in = {}
        
        for i,val in enumerate(inorder):
            dic_in[val] = i
            
        return build(0, length-1, 0, length-1)
