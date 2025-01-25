import unittest

import Sort
import Arrays

class TestSort(unittest.TestCase):
    def test_bubble_sort(self):
        test_arr = [1,6,3,8,4,9,2,0]                    # Случайные значения
        Sort.bubble_sort(test_arr)
        self.assertTrue(Arrays.is_sorted(test_arr))
        test_arr = [0,1,0,1,0,1]                        # Повторяющиеся чередующиеся значения
        Sort.bubble_sort(test_arr)
        self.assertTrue(Arrays.is_sorted(test_arr))
        test_arr = [1,1,1,1,1]                          # Одинаковые значения во всем массиве
        Sort.bubble_sort(test_arr)
        self.assertTrue(Arrays.is_sorted(test_arr))
        test_arr = [6,5,4,3,2,1,0]                      # Убывающие не повторяющиеся значения
        Sort.bubble_sort(test_arr)
        self.assertTrue(Arrays.is_sorted(test_arr))
        test_arr = [0,1,2,3,4,5,6]                      # Возрастающие не повторяющиеся значения
        Sort.bubble_sort(test_arr)
        self.assertTrue(Arrays.is_sorted(test_arr))

    def test_merge_sort(self):
        test_arr = [4,1,6,9,4,2]                    # Случайные значения
        test_arr = Sort.merge_sort(test_arr)
        self.assertTrue(Arrays.is_sorted(test_arr))
        test_arr = [2,3,2,3,2,3]                    # Повторяющиеся чередующиеся значения
        test_arr = Sort.merge_sort(test_arr)
        self.assertTrue(Arrays.is_sorted(test_arr))
        test_arr = [0,0,0,0,0]                      # Одинаковые значения во всем массиве
        test_arr = Sort.merge_sort(test_arr)
        self.assertTrue(Arrays.is_sorted(test_arr))
        test_arr = [9,8,7,6,5,4,3]                  # Убывающие не повторяющиеся значения
        test_arr = Sort.merge_sort(test_arr)
        self.assertTrue(Arrays.is_sorted(test_arr))
        test_arr = [0,1,2,3,4,5]                    # Возрастающие не повторяющиеся значения
        test_arr = Sort.merge_sort(test_arr)
        self.assertTrue(Arrays.is_sorted(test_arr))

    def test_quick_sort(self):
        test_arr = [9,6,0,3,1,4,2]
        Sort.quick_sort(test_arr, 0, len(test_arr) - 1)
        self.assertTrue(Arrays.is_sorted(test_arr))
        test_arr = [0,8,0,8,0]
        Sort.quick_sort(test_arr, 0, len(test_arr) - 1)
        self.assertTrue(Arrays.is_sorted(test_arr))
        test_arr = [9,9,9,9,9]
        Sort.quick_sort(test_arr, 0, len(test_arr) - 1)
        self.assertTrue(Arrays.is_sorted(test_arr))
        test_arr = [8,7,6,5,4,3,2,1,0]
        Sort.quick_sort(test_arr, 0, len(test_arr) - 1)
        self.assertTrue(Arrays.is_sorted(test_arr))
        test_arr = [0,1,2,3,4,5]
        Sort.quick_sort(test_arr, 0, len(test_arr) - 1)
        self.assertTrue(Arrays.is_sorted(test_arr))

    def test_shell_sort(self):
        test_arr = [2,6,2,7,4,1,0,5]
        Sort.shell_sort(test_arr)
        self.assertTrue(Arrays.is_sorted(test_arr))
        test_arr = [3,5,3,5,3,5]
        Sort.shell_sort(test_arr)
        self.assertTrue(Arrays.is_sorted(test_arr))
        test_arr = [1,1,1,1,1,1]
        Sort.shell_sort(test_arr)
        self.assertTrue(Arrays.is_sorted(test_arr))
        test_arr = [9,8,7,6,5,4,3,2,1]
        Sort.shell_sort(test_arr)
        self.assertTrue(Arrays.is_sorted(test_arr))
        test_arr = [0,1,2,3,4,5,6]
        Sort.shell_sort(test_arr)
        self.assertTrue(Arrays.is_sorted(test_arr))
        test_arr = [i for i in range(100, 0, -1)]
        print(test_arr)