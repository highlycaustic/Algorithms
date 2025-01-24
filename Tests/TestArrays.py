import os
import unittest

import Arrays


class TestArrays(unittest.TestCase):
    def test_random_list(self):
        low = 0                                                            # Нижний предел случайной генерации
        high = 10                                                          # Верхний предел
        test_arr = Arrays.random_list(low, high, 10)                  # Тестовый массив
        self.assertIsNotNone(test_arr)                                     # Проверка на создание массива
        self.assertTrue(test_arr)                                          # Массив не пустой
        self.assertTrue(any(x in range(low, high + 1) for x in test_arr))  # В массиве есть хотя бы одно сгенерированное значение

    def test_mono_raising_list(self):
        low = 1                                                            # Нижний предел случайной генерации
        high = 5                                                           # Верхний предел
        test_arr = Arrays.mono_raising_list(low, high, 10)            # Тестовый массив
        self.assertIsNotNone(test_arr)                                     # Проверка на создание массива
        self.assertTrue(test_arr)                                          # Массив не пустой
        self.assertTrue(any(x in range(low, high + 1) for x in test_arr))  # В массиве есть хотя бы одно сгенерированное значение
        self.assertTrue(test_arr[0] < test_arr[-1])                        # Последний элемент больше первого

    def test_is_sorted(self):
        test_arr = [0,1,2,3,4,5]                        # Тестовый массив
        self.assertTrue(Arrays.is_sorted(test_arr))     # Проверка сортировки в правильном порядке
        test_arr = [0,1,2,3,5,4]
        self.assertFalse(Arrays.is_sorted(test_arr))    # Проверка на неправильном порядке
        test_arr = [1,0,2,3,4,5]
        self.assertFalse(Arrays.is_sorted(test_arr))    # Проверка на неправильном порядке
        test_arr = [0] * 5
        self.assertTrue(Arrays.is_sorted(test_arr))     # Проверка на пустых элементах
        test_arr = [0,0,0,1,1,1]
        self.assertTrue(Arrays.is_sorted(test_arr))     # Проверка на возрастающих одинаковых элементах
        test_arr = [1,1,1,0,0,0]
        self.assertFalse(Arrays.is_sorted(test_arr))    # Проверка на убывающих одинаковых элементах

    def test_save_to_file(self):
        test_arr = [0,1,2,3,4,5]                                # Тестовый массив
        Arrays.save_to_file(test_arr,"testfile.txt")    # Запись в тестовый файл
        read_arr = []
        with open("testfile.txt", 'r') as f:                    # Чтение из файла в массив для сравнения
            for elem in f:
                read_arr.append(int(elem))
        self.assertEqual(test_arr, read_arr)                    # Сравнение тестового массива с вычитанным из файла
        os.remove("testfile.txt")                               # Чистка хвостов
