class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data  = data
        self.left  = None
        self.right = None
        self.left  = left
        self.right = right

def tree_into_list(node, _list):
    if node is not None:
        tree_into_list(node.left, _list)
        _list.append(node.data)
        tree_into_list(node.right, _list)

def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.data))
        print_tree(node.left, level + 1)

def node_lnr(TreeNode):
    if TreeNode is None:
        return
    node_lnr(TreeNode.left)
    print(TreeNode.data, end=' ')
    node_lnr(TreeNode.right)