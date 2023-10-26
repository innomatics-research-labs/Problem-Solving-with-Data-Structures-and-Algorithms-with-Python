class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def preorder(node):
            if node is None:
                return
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return result
