import unittest
from fib_heap import FibHeap

class Test_FibHeap(unittest.TestCase):
    def heap(self, add_order: list, expected_output: list):
        fb = FibHeap()
        cur_output = []

        for i in add_order:
            fb.add(i)

        while not fb.empty():
            cur_output.append(fb.extract_min())

        self.assertListEqual(expected_output, cur_output)

    def test_heap1(self):
        self.heap([
            1, 2, 3, 4
        ], [
            1, 2, 3, 4
        ])

    def test_heap2(self):
        self.heap([
            4, 2, 1, 3
        ], [
            1, 2, 3, 4
        ])

    def test_heap3(self):
        self.heap([
            4, 4, 3, 1, 3
        ], [
            1, 3, 3, 4, 4
        ])

    def test_heap4(self):
        self.heap([
            -1, -1, -1, -1, -1, -1, -1
        ], [
            -1, -1, -1, -1, -1, -1, -1
        ])

    def test_heap5(self):
        self.heap([
            1, 4, -10, 5, 0, 0, 0, 0, 0, 0
        ], [
            -10, 0, 0, 0, 0, 0, 0, 1, 4, 5
        ])

if __name__ == '__main__':
    unittest.main()