import unittest
import hw

class TestFunctions(unittest.TestCase):

    def test_squares(self):
        self.assertEqual(hw.squares(5), [0, 1, 4, 9, 16])
        self.assertEqual(hw.squares(0), [0])

    def test_unique_squares(self):
        self.assertEqual(hw.unique_squares([1, 2, 2, 3]), {1, 4, 9})

    def test_char_counts(self):
        self.assertEqual(hw.char_counts("hello"), {'h': 1, 'e': 1, 'l': 2, 'o': 1})

    def test_flatten(self):
        self.assertEqual(hw.flatten([[1, 2], [3, 4]]), [1, 2, 3, 4])

    def test_squares_gen(self):
        self.assertEqual(list(hw.squares_gen(3)), [0, 1, 4, 9])

    def test_odd_squares(self):
        self.assertEqual(hw.odd_squares(5), {1, 9, 25})

    def test_index_map(self):
        self.assertEqual(hw.index_map("abca"), {'a': 3, 'b': 1, 'c': 2})

    def test_unique_values(self):
        self.assertEqual(hw.unique_values([[1, 2], [2, 3]]), {1, 2, 3})

    def test_fibonacci_gen(self):
        self.assertEqual(list(hw.fibonacci_gen(5)), [0, 1, 1, 2, 3])

    def test_invert_dict(self):
        self.assertEqual(hw.invert_dict({'a': 1}), {1: 'a'})

    def test_primes(self):
        self.assertEqual(hw.primes(10), [2, 3, 5, 7])

    def test_intersection(self):
        self.assertEqual(hw.intersection([{1, 2}, {2, 3}]), {2})

    def test_factorials_gen(self):
        import math
        self.assertEqual(list(hw.factorials_gen(5)), [math.factorial(i) for i in range(5)])

    def test_str_lengths(self):
        self.assertEqual(hw.str_lengths(['hi']), {'hi': 2})

    def test_transpose(self):
        self.assertEqual(hw.transpose([[1, 2], [3, 4]]), [[1, 3], [2, 4]])

    def test_reverse_gen(self):
        self.assertEqual(list(hw.reverse_gen([1, 2, 3])), [3, 2, 1])

    def test_group_by_length(self):
        self.assertEqual(hw.group_by_length(['a', 'bb']), {1: ['a'], 2: ['bb']})

    def test_common_elements(self):
        self.assertEqual(hw.common_elements([[1, 2], [2, 3]]), {2})

    def test_primes_gen(self):
        self.assertEqual(list(hw.primes_gen(10)), [2, 3, 5, 7])

    def test_list_to_dict(self):
        self.assertEqual(hw.list_to_dict(['a', 'b']), {0: 'a', 1: 'b'})


if __name__ == "__main__":
    unittest.main()