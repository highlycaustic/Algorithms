import unittest

import Search


class TestSearch(unittest.TestCase):
    def test_seq_search(self):
        test_arr = [1,2,3,4,5]                                          # Массив с возрастающими не повторяющимися числами
        self.assertEqual(Search.seq_search(test_arr, 3), 2)
        self.assertEqual(Search.seq_search(test_arr, 5), 4)
        self.assertEqual(Search.seq_search(test_arr, 0), -1)
        test_arr = [0,1,0,1,2,2]                                        # Массив с повторяющимися числами
        self.assertEqual(Search.seq_search(test_arr, 1), 1)
        self.assertEqual(Search.seq_search(test_arr, 2), 4)
        self.assertEqual(Search.seq_search(test_arr, 0), 0)

    def test_bin_search(self):
        test_arr = [1,2,3,4,5]                                                                      # Массив с возрастающими не повторяющимися числами
        self.assertEqual(Search.bin_search(test_arr, 0, len(test_arr) - 1, 4), 3)
        self.assertEqual(Search.bin_search(test_arr, 0, len(test_arr) - 1, 1), 0)
        self.assertEqual(Search.bin_search(test_arr, 0, len(test_arr) - 1, 3), 2)
        self.assertEqual(Search.bin_search(test_arr, 0, len(test_arr) - 1, 7), -1)
        test_arr = [5,4,3,2,1]                                                                      # Массив с убывающими числами
        self.assertEqual(Search.bin_search(test_arr, 0, len(test_arr) - 1, 2), -1)
        self.assertEqual(Search.bin_search(test_arr, 0, len(test_arr) - 1, 5), -1)
        self.assertEqual(Search.bin_search(test_arr, 0, len(test_arr) - 1, 3), 2)
        test_arr = [0,0,0,1,1,1]                                                                    # Массив с возрастающими повторяющимися числами
        self.assertEqual(Search.bin_search(test_arr, 0, len(test_arr) - 1, 1), 4)
        self.assertEqual(Search.bin_search(test_arr, 0, len(test_arr) - 1, 0), 2)
