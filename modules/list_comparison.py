def find_differences_between_two_lists_and_sort_result(list1, list2):
    a = set(list1)
    b = set(list2)
    c = a.symmetric_difference(b)
    return sorted(list(c))