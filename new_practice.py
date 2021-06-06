from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    some_list = items.copy()
    if border in items:
        for i in items:
            if i != border:
             some_list.pop(0)
            else:
                break
    return some_list

if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5, 8, 9], 5)))

    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    # assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    # assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    # assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    # assert list(remove_all_before([], 0)) == []
    # assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    # print("Coding complete? Click 'Check' to earn cool rewards!")
