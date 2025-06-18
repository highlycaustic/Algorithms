import unittest

from AVLTrees import AVLTree, AVLNode
from BinTrees import BinSTree, TreeNode


class TestBinTrees(unittest.TestCase):
    def test_bin_s_trees(self):
        tree = BinSTree(TreeNode(5))        # Пень
        self.assertTrue(tree.search(5))     # Проверка поиска
        self.assertFalse(tree.search(-1))
        self.assertEqual(tree.count(), 1) # Проверка числа узлов
        self.assertEqual(tree.depth(), 0) # Проверка глубины

        for i in range(10):                 # Вырожденное дерево (только правая ветка)
            tree.insert_node(5 + i * 2)
        tree_iterated = []
        # Проверка итератора, дерево вырождено и без балансировки будет выведено в список сверху-вниз (по уровням)
        for node in tree:
            tree_iterated.append(node.data)
        # print(tree_iterated)
        # tree.print_tree()
        self.assertEqual(tree_iterated, [5, 7, 9, 11, 13, 15, 17, 19, 21, 23])
        self.assertTrue(tree.search(23))
        self.assertTrue(tree.root.left is None) # Проверка на вырожденность
        self.assertEqual(tree.count(), 10) # Проверка числа узлов
        self.assertEqual(tree.depth(), 9) # Проверка глубины

        tree2 = BinSTree()
        tree.copy(tree2)
        self.assertNotEqual(tree.root, tree2.root)              # Объекты узлов оригинала и копии не должны быть идентичны
        self.assertNotEqual(tree.root.right, tree2.root.right)  # Проверка первого правого узла копии
        self.assertEqual(tree.root.data, tree2.root.data)       # Проверка значения копии
        tree.delete()
        self.assertTrue(tree.root is None)
        tree.insert_node(1)
        self.assertEqual(tree.root.data, 1)

    def test_avl_trees(self):
        tree = AVLTree(AVLNode(5))        # Пень
        self.assertTrue(tree.search(5))     # Проверка поиска
        self.assertFalse(tree.search(-1))
        self.assertEqual(tree.count(), 1) # Проверка числа узлов
        self.assertEqual(tree.depth(), 0) # Проверка глубины

        for i in range(10):                 # Вырожденное дерево (только правая ветка)
            tree.insert_node(5 + i * 2)

       # Проверка итератора, дерево должно сбалансироваться при вставке узлов
        tree_iterated = []
        for node in tree:
            tree_iterated.append(node.data)
        # print(tree_iterated)
        # tree.print_tree()
        self.assertEqual(tree_iterated, [11, 7, 19, 5, 9, 15, 21, 13, 17, 23])
        self.assertTrue(tree.search(23))
        self.assertTrue(tree.root.left is not None) # АВЛ дерево не должно быть вырожденным
        self.assertEqual(tree.count(), 10) # Проверка числа узлов
        self.assertEqual(tree.depth(), 3) # Проверка глубины

        tree2 = BinSTree()
        tree.copy(tree2)
        self.assertNotEqual(tree.root, tree2.root)              # Объекты узлов оригинала и копии не должны быть идентичны
        self.assertNotEqual(tree.root.right, tree2.root.right)  # Проверка первого правого узла копии
        self.assertEqual(tree.root.data, tree2.root.data)       # Проверка значения копии
        tree.delete()
        self.assertTrue(tree.root is None)
        tree.insert_node(1)
        self.assertEqual(tree.root.data, 1)

        tree = AVLTree(AVLNode(5))
        tree.root.right = AVLNode(6)
        tree.root.right.right = AVLNode(8)
        tree.root.right.right.left = AVLNode(7)
        tree.root.right.right.right = AVLNode(9)
        tree.root.right.right.right.right = AVLNode(10)

        tree.print_tree()
        print("=" * 50)
        tree.rebalance_tree()
        tree.print_tree()

        tree_iterated = []
        for node in tree:
            tree_iterated.append(node.data)
        self.assertEqual(tree_iterated, [8, 5, 9, 6, 10, 7])

# TODO: BIG O в доках