import unittest

from .sift_up import sift_up
from .sift_down import sift_down

"""
- Binary tree. Parent's value >= children value
- Almost complete binary tree
- Difference between levels <= 1
- All leaves start from left
- arr[i div 2] <= arr[i]

            2
          /   \
        4      3
      /  \    /
     7    6  5


- Packing into array

              i
           /     \
         2i       2i+1
       /    \      /
     4i    4i+1   4i+2

- When we need to add element, add it to leaves and sift it up (to bubble) swapping with parent

"""


"""
Before:

         3
      4    2
    7   6  5  0

After:

         0
      4     3
    7   6  5  2

"""


class PriorityQueue:
    def __init__(self, arr):
        self.queue = []

        for el in arr:
            self.enqueue(el)

    def peek(self):
        if len(self.queue) == 0:
            return None

        return self.queue[0]

    def extract(self):
        result = self.peek()

        if result is None:
            return

        self.queue = sift_down(self.queue)

        return result

    def enqueue(self, el):
        self.queue.append(el)
        self.queue = sift_up(self.queue)

    def get_queue(self):
        return self.queue


class Test(unittest.TestCase):
    def test_priority_queue_set(self):
        q = PriorityQueue([1, 4, 2, 6, 4, 2, 0])
        result = q.get_queue()
        self.assertEqual(result, [0, 4, 1, 6, 4, 2, 2])

    def test_peek(self):
        q = PriorityQueue([1, 4, 2, 6, 4, 2, 0])
        result = q.peek()
        self.assertEqual(result, 0)

    def test_extract(self):
        q = PriorityQueue([1, 4, 2, 6, 4, 2, 0])
        result = q.extract()
        self.assertEqual(result, 0)

        result = q.extract()
        self.assertEqual(result, 1)

        result = q.extract()
        self.assertEqual(result, 2)

        result = q.extract()
        self.assertEqual(result, 2)

        result = q.extract()
        self.assertEqual(result, 4)

        result = q.extract()
        self.assertEqual(result, 4)

        result = q.extract()
        self.assertEqual(result, 6)

    def test_extract_from_empty(self):
        q = PriorityQueue([])
        result = q.extract()
        self.assertEqual(result, None)

    def test_enqueue(self):
        q = PriorityQueue([])
        q.enqueue(1)

        result = q.extract()

        self.assertEqual(result, 1)

        q.enqueue(1)
        q.enqueue(6)
        q.enqueue(0)

        result = q.extract()
        self.assertEqual(result, 0)

        result = q.extract()
        self.assertEqual(result, 1)

        result = q.extract()
        self.assertEqual(result, 6)

        result = q.extract()
        self.assertEqual(result, None)


if (__name__ == '__main__'):
    unittest.main()
