from random import randint


class TreeNode:
    """
    Класс узла бинарного дерева
    """
    def __init__(self, data, left = None, right = None):
        self.data  = data
        self.left  = left
        self.right = right

def insert_node(node: TreeNode, value):
    """
    Вставка узла в дерево
    :param node: корневой узел дерева, в которое нужно вставить занчение
    :param value: значение для вставки
    :return: None
    """
    if node.data == value:
        print(f"Встречен дубликат ({value}), значение не вставлено")
    else:
        if node.data > value:
            if node.left is not None:
                insert_node(node.left, value)
            else:
                node.left = TreeNode(value)
        else:
            if node.right is not None:
                insert_node(node.right, value)
            else:
                node.right = TreeNode(value)

def tree_depth(node: TreeNode):
    """
    Рекурсивно считает глубину дерева в уровнях
    :param node: Корневой узел бинарного дерева
    :return: Целое число уровней дерева
    """
    if node is None:
        return -1
    depth_left = tree_depth(node.left)
    depth_right = tree_depth(node.right)

    return max(depth_left, depth_right) + 1

def tree_count(node: TreeNode):
    """
    Рекурсивно считает количество узлов в дереве
    :param node: Корневой узел бинарного дерева
    :return: Целое число узлов дерева
    """
    if node is None:
        return 0
    return tree_count(node.left) + tree_count(node.right) + 1

def print_tree(node: TreeNode, level=0):
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

def tree_into_list(node: TreeNode, _list):
    """
    Заполняет список узлами дерева в порядке обхода. Обходит по порядку LNR
    :param node: корневой узел дерева
    :param _list: список для заполнения
    :return: None
    """
    if node is not None:
        tree_into_list(node.left, _list)
        _list.append(node)
        tree_into_list(node.right, _list)

def get_successor(node: TreeNode):
    """
    Поиск следующего наибольшего узла в дереве
    :param node: Узел, для которого ищется следующее наибольшее
    :return: Следующее наибольшее TreeNode
    """
    curr_node = node.right
    while curr_node is not None and curr_node.left is not None:
        curr_node = curr_node.left
    return curr_node

def remove_node(node: TreeNode, value):
    """
    Удаляет узел дерева
    :param node: Корневой узел
    :param value: Значение, по которому нужно удалить узел
    :return: TreeNode измененного корневого узла
    """
    # Рекурсивно искать слева и справа пока не наткнемся на нужное значение
    if node.data > value:
        node.left = remove_node(node.left, value)
    elif node.data < value:
        node.right = remove_node(node.right, value)
    else: # если значение = значению узла
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
        node.right = remove_node(node.right, successor.data)
    # Возвращаем предку измененный узел
    return node

def search(node: TreeNode, value):
    """
    Поиск по бинарному дереву
    :param node: Корневой узел дерева
    :param value: Значение, которое нужно найти
    :return: TreeNode узла, в котором найдено значение, и None, если не найдено
    """
    if node is None or node.data == value:
        return node
    if node.data < value:
        return search(node.right, value)
    return search(node.left, value)

def delete(node: TreeNode):
    """
    Полная рекурсивная очистка дерева
    :param node: Корневой узел, с которого начать очистку
    :return: Измененный узел, "пень", очищенный от поддерева
    """
    if node is not None:
        delete(node.left)
        delete(node.right)

        node.left = None
        node.right = None

def copy_node(node1):
    """
    Глубокое копирование дерева
    :param node1: Корневой узел копируемого дерева
    :return: Корневой узел скопированного дерева (результат)
    """
    if node1 is None:
        return None
    node2 = TreeNode(node1.data)
    node2.left = copy_node(node1.left)
    node2.right = copy_node(node1.right)
    return node2

def populate_nodes(node: TreeNode, size, min, max):
    """
    Заполняет дерево целыми случайными значениями по заданным параметрам размера
    :param node: Корневой узел дерева
    :param size: Размер дерева
    :param min: Минимальный порог случайных значений
    :param max: Максимальный порог случайных значений
    :return: None
    """
    for i in range(size):
        insert_node(node, randint(min, max))


class BinSTreeIterator:
    """
    Класс-итератор для бинарных деревьев
    """
    def __init__(self, node: TreeNode):
        """
        Конструктор
        :param node: Корневой узел дерева
        """
        self.treelist = []                  # объявляем пустой список для дерева
        self.current = 0                    # счетчик текущего положения итератора
        tree_into_list(node, self.treelist) # переливаем дерево в список

    def __iter__(self):
        return self

    def __next__(self):
        """
        Операция перехода к след. элементу
        :return: Следующий узел дерева
        """
        if self.current < len(self.treelist):
            result = self.treelist[self.current]
            self.current += 1
            return result
        raise StopIteration

class BinSTree:
    """
    Класс бинарного дерева
    """
    def __init__(self, root_node: TreeNode = None):
        """
        Конструктор
        :param root_node: Корневой узел дерева
        """
        self.root = root_node

    def __iter__(self):
        """
        Итератор
        :return: Объект итератора BinSTreeIterator
        """
        return BinSTreeIterator(self.root)

    def print_tree(self, level = 0):
        """
        Выводит дерево в консоль
        :param level: Уровень, с которого начать печать (по умолчанию 0)
        :return: None
        """
        print_tree(self.root, level)

    def tree_into_list(self, _list):
        """
        Заполняет список узлами дерева
        :param _list: Список для заполнения
        :return: None
        """
        tree_into_list(self.root, _list)

    def insert_node(self, value):
        """
        Вставка узла в дерево
        :param value: Значение для вставки
        :return: None
        """
        if self.root is None:
            self.root = TreeNode(value)
        else:
            insert_node(self.root, value)

    def remove_node(self, value):
        """
        Удаление узла из дерева
        :param value: Значение для удаления
        :return: None
        """
        if self.root is None:
            print("Дерево пустое")
        else:
            remove_node(self.root, value)

    def search(self, value):
        """
        Поиск в дереве
        :param value: Значение, которое нужно найти
        :return: None
        """
        if search(self.root, value):
            print("Значение присутствует в дереве")
        else:
            print("Значение не найдено")

    def delete(self):
        """
        Удаление дерева
        :return: None
        """
        delete(self.root)
        self.root = None

    def copy(self, target):
        """
        Копирование дерева в другое дерево
        :param target: Целевое дерево
        :return: None
        """
        if target.root is not None:
            target.delete()
        target.root = copy_node(self.root)

    def depth(self):
        """
        Глубина дерева
        :return: Глубина дерева в int
        """
        return tree_depth(self.root)

    def count(self):
        """
        Количество узлов в дереве
        :return: Количество узлов в дереве в int
        """
        return tree_count(self.root)

    def rand_spawn(self, size, min, max):
        """
        Заполняет дерево случайными значениями
        :param size: Размер дерева
        :param min: Нижний порог случайных значений
        :param max: Верхний порог случайных значений
        :return:None
        """
        self.root = TreeNode(randint(min, max))
        populate_nodes(self.root, size, min, max)
