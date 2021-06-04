import unittest


def sift_down(arr):
    arr[0] = arr[-1]
    arr.pop()

    i = 0

    while (2 * (i + 1) < len(arr)):
        next_child_idx = child(arr, i)

        if next_child_idx == i:
            break

        t = arr[i]
        arr[i] = arr[next_child_idx]
        arr[next_child_idx] = t

        i = next_child_idx

    return arr


def child(arr, i):
    min = i
    first_child_idx = (i + 1) * 2 - 1
    last_child_idx = (i + 1) * 2

    if len(arr) > first_child_idx and arr[first_child_idx] < arr[i]:
        min = first_child_idx

    if len(arr) > last_child_idx and arr[last_child_idx] < arr[min]:
        min = last_child_idx

    return min


class Test(unittest.TestCase):
    def test_sift_down_one_level_first_is_less(self):
        result = sift_down([0, 1, 6, 10])
        self.assertEqual(result, [1, 10, 6])

    def test_sift_down_one_level_second_is_less(self):
        result = sift_down([0, 6, 1, 10])
        self.assertEqual(result, [1, 6, 10])

    def test_sift_down_root_is_less(self):
        result = sift_down([0, 10, 20, 1])
        self.assertEqual(result, [1, 10, 20])

    def test_sift_down_deep_tree(self):
        result = sift_down([0, 5, 3, 10, 20, 40, 7])
        self.assertEqual(result, [3, 5, 7, 10, 20, 40])


if __name__ == "__main__":
    unittest.main()
