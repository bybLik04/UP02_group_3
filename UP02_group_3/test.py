import unittest
import numpy as np
import os
from approx_2dg import combine, calc, toFixed
from approx_1dg import calculate_linear_regression, plot_graph

class TestApproximation(unittest.TestCase):
    
    def test_combine(self):
        test_data = [
            ([1, 3, 2], [4, 6, 5], [1, 2, 3], [4, 5, 6]),
            ([2, 4, 6], [8, 10, 12], [2, 4, 6], [8, 10, 12]),
        ]
        
        for x_arr, y_arr, expected_x, expected_y in test_data:
            x, y = combine(x_arr, y_arr)
            self.assertEqual(list(x), expected_x)
            self.assertEqual(list(y), expected_y)
    
    def test_calc(self):
        test_data = [
            (np.array([1, 2, 3]), np.array([4, 5, 6]), 0.0, 1.0, 3.0, 1.0),
            (np.array([2, 4, 6]), np.array([8, 10, 12]), 0.0, 1.0, 6.0, 1.0),
        ]
        
        for x, y, expected_k, expected_b, expected_c, expected_r2 in test_data:
            k, b, c, r2 = calc(x, y)
            self.assertAlmostEqual(k, expected_k, places=7)
            self.assertAlmostEqual(b, expected_b, places=7)
            self.assertAlmostEqual(c, expected_c, places=7)
            self.assertAlmostEqual(r2, expected_r2, places=7)

    def test_toFixed(self):
        test_data = [
            (3.14159, '3.142'),
            (2.71828, '2.718'),
        ]
        
        for num, expected_fixed_num in test_data:
            fixed_num = toFixed(num)
            self.assertEqual(fixed_num, expected_fixed_num)

class TestCalculateLinearRegression(unittest.TestCase):
    def test_calculate_linear_regression(self):
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([2, 4, 6, 8, 10])
        expected_k = 2.0
        expected_b = 0.0
        expected_r2 = 1.0

        k, b, r2 = calculate_linear_regression(x, y)

        self.assertEqual(k, expected_k)
        self.assertEqual(b, expected_b)
        self.assertEqual(r2, expected_r2)


class TestPlotGraph(unittest.TestCase):
    def test_plot_graph(self):
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([2, 4, 6, 8, 10])
        k = 2.0
        b = 0.0

        plot_graph(x, y, k, b)

        self.assertTrue(os.path.exists('static/images/graph5.png'))

    def test_plot_graph_empty_data(self):
        x = np.array([])
        y = np.array([])
        k = 2.0
        b = 0.0

        plot_graph(x, y, k, b)

        self.assertTrue(os.path.exists('static/images/graph5.png'))

    def test_plot_graph_single_point(self):
        x = np.array([1])
        y = np.array([2])
        k = 2.0
        b = 0.0

        plot_graph(x, y, k, b)

        self.assertTrue(os.path.exists('static/images/graph5.png'))

if __name__ == '__main__':
    unittest.main()