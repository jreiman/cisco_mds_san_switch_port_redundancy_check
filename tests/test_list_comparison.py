import unittest
from modules.list_comparison import find_differences_between_two_lists_and_sort_result

differences = find_differences_between_two_lists_and_sort_result

class test_list_comparison(unittest.TestCase):
    list1_sorted = ['fc1/1', 'fc1/2', 'fc2/1', 'fc2/2']
    list1_unsorted = ['fc1/1', 'fc2/1', 'fc2/2', 'fc1/2']
    list2_sorted = ['fc1/1', 'fc1/3', 'fc2/1', 'fc2/3']
    list2_unsorted = ['fc1/1', 'fc2/1', 'fc1/3', 'fc2/3']
    result_list1_list2 = ['fc1/2', 'fc1/3', 'fc2/2', 'fc2/3']
    result_identical_list = []

    def test_two_sorted_lists(self):
        self.assertEqual(differences(self.list1_sorted, self.list2_sorted), self.result_list1_list2)

    def test_two_unsorted_lists(self):
        self.assertEqual(differences(self.list1_unsorted, self.list2_unsorted), self.result_list1_list2)

    def test_two_identical_lists_in_same_order(self):
        self.assertEqual(differences(self.list1_sorted, self.list1_sorted), self.result_identical_list)

    def test_two_identical_lists_in_different_order(self):
        self.assertEqual(differences(self.list2_sorted, self.list2_unsorted), self.result_identical_list)              


if __name__ == '__main__':
    unittest.main()