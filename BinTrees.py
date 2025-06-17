class TreeNode:
    """
    Класс узла бинарного дерева
    """
    def __init__(self, data, left = None, right = None):
        self.data  = data
        self.left  = left
        self.right = right

def tree_into_list(node, _list):
    """
    Заполняет список узлами дерева в порядке обхода. Обходит по порядку LNR
    :param node: корневой узел дерева
    :param _list: список для заполнения
    :return: None
    """
    if node is not None:
        tree_into_list(node.left, _list)
        _list.append(node.data)
        tree_into_list(node.right, _list)

def print_tree(node, level=0):
    """
    Выводит дерево в консоль слева направо, где слева - корень
    :param node: корневой узел дерева
    :param level: уровень, с которого начать вывод
    :return: None
    """
    if node is not None:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.data))
        print_tree(node.left, level + 1)


def insert_node(node: TreeNode, key):
    """
    Вставка узла в дерево
    :param node: корневой узел дерева, в которое нужно вставить занчение
    :param key: значение для вставки
    :return: None
    """
    if node.data == key:
        print("Встречен дубликат, значение не вставлено")
    if node.data > key:
        if node.left is not None:
            insert_node(node.left, key)
        else:
            node.left = TreeNode(key)
    if node.data < key:
        if node.right is not None:
            insert_node(node.right, key)
        else:
            node.right = TreeNode(key)
