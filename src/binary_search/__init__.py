import unittest


def binary_search(arr, x):
    l = 0
    r = len(arr) - 1

    while l < r:
        mid = (l + r) // 2

        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid

    return l if arr[l] == x else -1


def binary_search_with_fake_elements(arr, x):
    l = -1
    r = len(arr)

    while l < r - 1:
        mid = (l + r) // 2

        if arr[mid] >= x:
            r = mid
        else:
            l = mid

    return r if r < len(arr) and arr[r] == x else -1


class Test(unittest.TestCase):
    def test_binary_search_left(self):
        result = binary_search([1, 2, 3], 1)
        result2 = binary_search_with_fake_elements([1, 2, 3], 1)

        self.assertEqual(result, 0)
        self.assertEqual(result2, 0)

    def test_binary_search_right(self):
        result = binary_search([1, 2, 3], 3)
        result2 = binary_search_with_fake_elements([1, 2, 3], 3)

        self.assertEqual(result, 2)
        self.assertEqual(result2, 2)

    def test_binary_search_middle(self):
        result = binary_search([1, 2, 3], 2)
        result2 = binary_search_with_fake_elements([1, 2, 3], 2)

        self.assertEqual(result, 1)
        self.assertEqual(result2, 1)

    def test_binary_search_middle_even_first(self):
        result = binary_search([1, 2, 3, 4], 2)
        result2 = binary_search_with_fake_elements([1, 2, 3, 4], 2)

        self.assertEqual(result, 1)
        self.assertEqual(result2, 1)

    def test_binary_search_middle_even_second(self):
        result = binary_search([1, 2, 3, 4], 3)
        result2 = binary_search_with_fake_elements([1, 2, 3, 4], 3)

        self.assertEqual(result, 2)
        self.assertEqual(result2, 2)

    def test_binary_search_sequence(self):
        result = binary_search([0, 1, 2, 2, 2, 2, 3, 4], 2)
        result2 = binary_search_with_fake_elements([0, 1, 2, 2, 2, 2, 3, 4], 2)

        self.assertEqual(result, 2)
        self.assertEqual(result2, 2)

    def test_binary_search_not_found(self):
        result = binary_search([1, 2, 3, 4], 5)
        result2 = binary_search_with_fake_elements([1, 2, 3, 4], 5)

        self.assertEqual(result, -1)
        self.assertEqual(result2, -1)


unittest.main()
