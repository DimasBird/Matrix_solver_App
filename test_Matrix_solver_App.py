import unittest
import pytest
from Matrix_solver_App import MyCalcApp


class messageTest(unittest.TestCase):
    def test_div_conv(self):
        self.assertEqual(MyCalcApp.division_converter(self, '1/2'), [1, 2])
        self.assertEqual(MyCalcApp.division_converter(self, '1 + 3/2'), [5, 2])
        self.assertEqual(MyCalcApp.division_converter(self, '4 4/8'), [9, 2])
        self.assertEqual(MyCalcApp.division_converter(self, '0'), [0, 1])
        self.assertEqual(MyCalcApp.division_converter(self, '-5'), [-5, 1])
        self.assertEqual(MyCalcApp.division_converter(self, '-10.5'), [-21, 2])

        with pytest.raises(ValueError):
            MyCalcApp.division_converter(self, 'abc')
        with pytest.raises(ValueError):
            MyCalcApp.division_converter(self, '1 1')

    def test_nods(self):
        self.assertEqual(MyCalcApp.nod_decreaser(self, [0, 4]), [0, 1])
        self.assertEqual(MyCalcApp.nod_decreaser(self, [4, 2]), [2, 1])
        self.assertEqual(MyCalcApp.nod_decreaser(self, [-25, 5]), [-5, 1])
        self.assertEqual(MyCalcApp.nod_decreaser(self, [-31 * 59 * 4 * 9, 31 * 4 * 3 * 15 * 7]), [-59, 35])

    def test_n_returner(self):
        self.assertEqual(MyCalcApp.number_returner(self, [0, 1]), '0')
        self.assertEqual(MyCalcApp.number_returner(self, [-5, 1]), '-5')
        self.assertEqual(MyCalcApp.number_returner(self, [5, 2]), '5/2')

    def test_sorter(self):
        self.assertEqual(MyCalcApp.sorter(self, [[[1, 1], [1, 1], [2, 1]], [[0, 1], [1, 1], [1, 1]]], 0, 0),
                         [[[1, 1], [1, 1], [2, 1]], [[0, 1], [1, 1], [1, 1]]])
        self.assertEqual(MyCalcApp.sorter(self, [[[0, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [2, 1]]], 0, 0),
                         [[[1, 1], [1, 1], [2, 1]], [[0, 1], [1, 1], [1, 1]]])

    def test_math(self):
        self.assertEqual(MyCalcApp.math(self, [0, 1], [4, 3]), [4, 3])
        self.assertEqual(MyCalcApp.math(self, [-4, 1], [4, 1]), [0, 1])
        self.assertEqual(MyCalcApp.math(self, [1, 2], [1, 3]), [5, 6])
        self.assertEqual(MyCalcApp.math(self, [138, 7], [15, 28]), [81, 4])

    def test_divider(self):
        self.assertEqual(MyCalcApp.divider(self, [1, 2], [1, 2]), [1, 1])
        self.assertEqual(MyCalcApp.divider(self, [3, 2], [1, 2]), [3, 1])
        self.assertEqual(MyCalcApp.divider(self, [5, 2], [7, 3]), [15, 14])
        self.assertEqual(MyCalcApp.divider(self, [9, 4], [3, 2]), [3, 2])

    def test_mult(self):
        self.assertEqual(MyCalcApp.multiplier(self, [1, 2], [1, 2]), [1, 4])
        self.assertEqual(MyCalcApp.multiplier(self, [3, 2], [1, 3]), [1, 2])
        self.assertEqual(MyCalcApp.multiplier(self, [56, 3], [27, 8]), [63, 1])
        self.assertEqual(MyCalcApp.multiplier(self, [0, 1], [1, 2]), [0, 1])

    def test_Gauss(self):
        self.assertEqual(MyCalcApp.Gauss(self, [[[1, 1], [1, 1], [2, 1]], [[0, 1], [1, 1], [1, 1]]], 3, 2),
                         'x1 = 1, x2 = 1.')
        self.assertEqual(MyCalcApp.Gauss(self, [[[1, 1], [1, 1], [2, 1]], [[0, 1], [0, 1], [1, 1]]], 3, 2),
                         'Данная система не имеет решений.')
        self.assertEqual(MyCalcApp.Gauss(self, [[[1, 1], [1, 1], [2, 1]]], 3, 1), 'x1 = 2 - x2, x2 - любой.')


if __name__ == "__main__":
    unittest.main()
