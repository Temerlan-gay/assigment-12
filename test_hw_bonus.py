import unittest
import hw_bonus

class TestBonus(unittest.TestCase):

    def test_sieve(self):
        self.assertEqual(hw_bonus.sieve_of_eratosthenes(10), [2, 3, 5, 7])

    def test_triples(self):
        self.assertEqual(
            hw_bonus.triple_combinations([1, 2, 3, 4]),
            [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
        )

    def test_dict_table(self):
        self.assertEqual(hw_bonus.dict_table(2), {1: {1: 1, 2: 2}, 2: {1: 2, 2: 4}})

    def test_generators(self):
        self.assertEqual(list(map(list, hw_bonus.generators(2))), [[1, 2], [1, 2]])

    def test_cartesian(self):
        self.assertEqual(hw_bonus.cartesian_product([1], ['a']), [(1, 'a')])


if __name__ == "__main__":
    unittest.main()