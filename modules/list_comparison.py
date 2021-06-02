def find_differences_between_two_lists_and_sort_result(list1, list2):
    if not list1 and not list2:
        raise ValueError("Both lists are empty.")
    elif not list1:
        raise ValueError("list1 is empty.")
    elif not list2:
        raise ValueError("list2 is empty.")
    else:
        a = set(list1)
        b = set(list2)
        c = a.symmetric_difference(b)
        return sorted(list(c))