import unittest

"""
    JavaScript Example:

    function addToSorted(arr, x) {
        i = arr.length

        while(i > 0 && arr[i - 1] > x) {
            arr[i] = arr[i - 1]
            i--;
        }

        arr[i] = x

        return arr;
    }
"""


def add_to_sorted(arr, x):
    arr.append(x)

    i = len(arr) - 1

    while i > 0 and arr[i] < arr[i - 1]:
        t = arr[i]
        arr[i] = arr[i - 1]
        arr[i - 1] = t

        i -= 1

    return arr


class Test(unittest.TestCase):
    def test_add_to_sorted(self):
        result = add_to_sorted([1, 3, 4, 5], 2)
        self.assertListEqual(result, [1, 2, 3, 4, 5])

    def test_add_to_sorted_without_holes(self):
        result = add_to_sorted([1, 2, 3, 4, 5], 2)
        self.assertListEqual(result, [1, 2, 2, 3, 4, 5])

    def test_add_to_sorted_first(self):
        result = add_to_sorted([1, 2, 3, 4, 5], 0)
        self.assertListEqual(result, [0, 1, 2, 3, 4, 5])

    def test_add_to_sorted_last(self):
        result = add_to_sorted([1, 2, 3, 4, 5], 6)
        self.assertListEqual(result, [1, 2, 3, 4, 5, 6])


unittest.main()
