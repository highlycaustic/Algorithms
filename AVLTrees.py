from random import randint

from BinTrees import TreeNode, BinSTree, get_successor, remove_node


class AVLNode(TreeNode):
    """
    Класс узла АВЛ-дерева, унаследован от узла бинарного дерева, добавлено поле height высоты узла
    """
    def __init__(self, data):
        super().__init__(data)
        self.height = 1


def get_height(node):
    """
    Получить высоту узла
    :param node: Узел
    :return: Высота
    """
    if not node:
        return 0
    return node.height

def get_balance(node):
    """
    Получить баланс-фактор узла
    :param node: Узел
    :return: Баланс фактор
    """
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

 #     z                           y
 #    / \     Right Rotation      /  \
 #   y   T3   - - - - - - - >    T1   z
 #  / \       < - - - - - - -        / \
 # T1  T2     Left Rotation        T2  T3

def right_rotate(z):
    """
    Правый поворот, "поднимает" левого потомка y узла z, перевешивает правого потомка узла y вместо левого потомка z
    :param z: Опорный узел для поворота
    :return: Новый корневой узел дерева y класса AVLNode
    """
    y = z.left
    t2 = y.right

    y.right = z
    z.left = t2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def left_rotate(y):
    """
    Левый поворот, "поднимает" правого потомка z узла y, перевешивает левого потомка узла z вместо правого потомка y
    :param y: Опорный узел для поворота
    :return: Новый корневой узел дерева z класса AVLNode
    """
    z = y.right
    t2 = z.left

    z.left = y
    y.right = t2

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    z.height = 1 + max(get_height(z.left), get_height(z.right))

    return z

def update_height(node):
    """
    Обновляет высоту узла в соответствии с его поддеревьями
    :param node: Узел для обновления высоты
    :return: None
    """
    node.height = 1 + max(get_height(node.left), get_height(node.right))

def rebalance(node):
    """
    Балансировка дерева
    :param node: Корневой узел для балансировки
    :return: Сбалансированное дерево с корнем AVLNode
    """
    if node is None:
        return None

    node.left = rebalance(node.left)
    node.right = rebalance(node.right)
    # Обновляем высоту узла
    update_height(node)
    # Баланс фактор
    balance = get_balance(node)

    # Перевес в левую сторону
    if balance > 1:
        if get_balance(node.left) < 0:          # Поворот лево-право
            node.left = left_rotate(node.left)
        return right_rotate(node)               # Поворот лево-лево
    # Перевес в правую сторону
    if balance < -1:
        if get_balance(node.right) > 0:             # Поворот право-лево
            node.right = right_rotate(node.right)
        return left_rotate(node)                    # Поворот право-право

    return node

def insert_node_avl(node, value):
    """
    Вставка узла в АВЛ-дерево
    :param node: Корневой узел дерева
    :param value: Значение для вставки
    :return: Корневой узел дерева со вставленным значением
    """
    if not node:
        return AVLNode(value)

    if value < node.data:
        node.left = insert_node_avl(node.left, value)
    elif value > node.data:
        node.right = insert_node_avl(node.right, value)

    # Балансировка
    return rebalance(node)


def remove_node_avl(node, value):
    """
    Удаление узла в АВЛ-дереве
    :param node: Корневой узел дерева
    :param value: Значение для удаления
    :return: Корневой узел дерева с удаленным значением
    """
    if not node:
        return node

    if value < node.data:
        node.left = remove_node_avl(node.left, value)
    elif value > node.data:
        node.right = remove_node_avl(node.right, value)
    else:  # если значение = значению узла
        # Если потомком нет или есть только правый
        if node.left is None:
            # Передаем предку правое поддерево (вырезаем текущий узел)
            return node.right
        # Зеркально прошлому
        if node.right is None:
            # Передаем левое поддерево
            return node.left

        # Если есть оба потомка
        # Находим следующее наибольшее
        successor = get_successor(node)
        # Заменяем значение текущего узла значением и следующего наибольшего
        # (подменяем)
        node.data = successor.data
        # Удаляем следующее наибольшее
        node.right = remove_node_avl(node.right, successor.data)

    return rebalance(node)

def populate_nodes_avl(node, size, min, max):
    """
    Заполняет дерево целыми случайными значениями по заданным параметрам размера
    :param node: Корневой узел дерева
    :param size: Размер дерева
    :param min: Минимальный порог случайных значений
    :param max: Максимальный порог случайных значений
    :return: None
    """
    for i in range(size):
        insert_node_avl(node, randint(min, max))


class AVLTree(BinSTree):
    """
    Класс АВЛ-дерева, унаследован от бинарного дерева
    """
    def __init__(self, root_node: AVLNode):
        """Конструктор унаследован от бинарного дерева"""
        super().__init__(root_node)

    def rebalance_tree(self):
        """
        Балансирует дерево
        :return: None
        """
        self.root = rebalance(self.root)

    def insert_node(self, value):
        """
        Вставка значения в дерево
        :param value: Значение для вставки
        :return: None
        """
        self.root = insert_node_avl(self.root, value)

    def remove_node(self, value):
        """
        Удаление узла по значению
        :param value: Значение для удаления
        :return: None
        """
        self.root = remove_node_avl(self.root, value)

    def rand_spawn(self, size, min, max):
        """
        Заполнение дерева случайными значениями в заданном диапазоне
        :param size: Размер дерева
        :param min: Нижний предел случайных чисел
        :param max: Верхний предел случайных чисел
        :return: None
        """
        self.root = AVLNode(randint(min, max))
        populate_nodes_avl(self.root, size, min, max)
