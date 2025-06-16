class TreeNode:
    def __init__(self, data):
        self.data  = data
        self.left  = None
        self.right = None

def node_lnr(TreeNode):
    if TreeNode is None:
        return
    node_lnr(TreeNode.left)
    print(TreeNode.data, end=' ')
    node_lnr(TreeNode.right)