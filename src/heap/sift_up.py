import unittest


def sift_up(arr):
    i = len(arr) - 1

    def parent(x): return (x // 2) - 1 if x % 2 == 0 else x // 2

    while i > 0 and arr[i] < arr[parent(i)]:
        t = arr[i]
        arr[i] = arr[parent(i)]
        arr[parent(i)] = t
        i = parent(i)

    return arr


class Test(unittest.TestCase):
    def test_sift_up_full_tree(self):
        result = sift_up([2, 4, 3, 7, 6, 5, 0])
        self.assertEqual(result, [0, 4, 2, 7, 6, 5, 3])

    def test_sift_up_not_full_tree(self):
        result = sift_up([2, 4, 3, 7, 6, 0])
        self.assertEqual(result, [0, 4, 2, 7, 6, 3])

    def test_sift_up_new_level(self):
        result = sift_up([1, 4, 2, 7, 6, 3, 4, 0])
        self.assertEqual(result, [0, 1, 2, 4, 6, 3, 4, 7])

    def test_sift_up_not_needed(self):
        result = sift_up([1, 4, 2, 7, 6, 3, 4, 100])
        self.assertEqual(result, [1, 4, 2, 7, 6, 3, 4, 100])

    def test_sift_up_only_one_element(self):
        result = sift_up([0])
        self.assertEqual(result, [0])

    def test_sift_up_only_two_levels(self):
        result = sift_up([1, 0])
        self.assertEqual(result, [0, 1])


if __name__ == "__main__":
    unittest.main()
