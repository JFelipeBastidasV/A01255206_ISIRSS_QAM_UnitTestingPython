import unittest
from math_stats import *

class TestStats(unittest.TestCase):
    def test_add(self):
        # 1 : setup
        a, b = 2, 12 

        # 2 : expected outputs
        res = 14

        # 3 : assertion
        self.assertEqual(
            add(a, b),
            res,
            "add function is not working as expected")

    def test_add2(self):
        # 1 : setup
        a, b = 6, -12 

        # 2 : expected outputs
        res = -6

        # 3 : assertion
        self.assertEqual(
            add(a, b),
            res,
            "add function is not working as expected")

    def test_add3(self):
        # 1 : setup
        a, b = -18, -482

        # 2 : expected outputs
        res = -500

        # 3 : assertion
        self.assertEqual(
            add(a, b),
            res,
            "add function is not working as expected")

    def test_add4(self):
        # 1 : setup
        a, b = 100,10  

        # 2 : expected outputs
        res = 110

        # 3 : assertion
        self.assertEqual(
            add(a, b),
            res,
            "add function is not working as expected")

    def test_subtract(self):
        # 1 : setup
        a, b = 100,10  

        # 2 : expected outputs
        res = 90

        # 3 : assertion
        self.assertEqual(
            subtract(a, b),
            res,
            "subtract function is not working as expected")
        
    def test_subtract2(self):
        # 1 : setup
        a, b = -10,10  

        # 2 : expected outputs
        res = -20

        # 3 : assertion
        self.assertEqual(
            subtract(a, b),
            res,
            "subtract function is not working as expected")
        
    def test_subtract3(self):
        # 1 : setup
        a, b = 10, 10 

        # 2 : expected outputs
        res = 0

        # 3 : assertion
        self.assertEqual(
            subtract(a, b),
            res,
            "subtract function is not working as expected")
        
    def test_subtract4(self):
        # 1 : setup
        a, b = -100, -80 

        # 2 : expected outputs
        res = -20

        # 3 : assertion
        self.assertEqual(
            subtract(a, b),
            res,
            "subtract function is not working as expected")
        
    def test_multiply(self):
        # 1 : setup
        a, b = 10,"s" 

        # 2 : expected outputs
        res = "ssssssssss"

        # 3 : assertion
        self.assertEqual(
            multiply(a, b),
            res,
            "multiply function is not working as expected")

    def test_multiply2(self):
        # 1 : setup
        a, b = -10,10  

        # 2 : expected outputs
        res = -100

        # 3 : assertion
        self.assertEqual(
            multiply(a, b),
            res,
            "multiply function is not working as expected")
        
    def test_multiply3(self):
        # 1 : setup
        a, b = 1, 10

        # 2 : expected outputs
        res = 10

        # 3 : assertion
        self.assertEqual(
            multiply(a, b),
            res,
            "multiply function is not working as expected")
        
    def test_multiply4(self):
        # 1 : setup
        a, b = -12,-12  

        # 2 : expected outputs
        res = 144

        # 3 : assertion
        self.assertEqual(
            multiply(a, b),
            res,
            "multiply function is not working as expected")
        
    def test_divide(self):
        # 1 : setup
        a, b = -10,10  

        # 2 : expected outputs
        res = -1

        # 3 : assertion
        self.assertEqual(
            divide(a, b),
            res,
            "divide function is not working as expected")
        
    def test_divide2(self):
        # 1 : setup
        a, b = 100, 2  

        # 2 : expected outputs
        res = 50

        # 3 : assertion
        self.assertEqual(
            divide(a, b),
            res,
            "divide function is not working as expected")
        
    def test_divide3(self):
        # 1 : setup
        a, b = 19,3  

        # 2 : expected outputs
        res = 6.333333333333333

        # 3 : assertion
        self.assertEqual(
            divide(a, b),
            res,
            "divide function is not working as expected")

    def test_divide4(self):
        # 1 : setup
        a, b = 0, 0

        # 2 : expected outputs
        res = 0

        # 3 : assertion
        with self.assertRaises(ValueError):
            divide(a, b)
        
    def test_power(self):
        self.assertEqual(power(2,10), 1024)

    def test_power2(self):
        self.assertEqual(power(3,3), 27)
    
    def test_power3(self):
        self.assertEqual(power(5,0),1)

    def test_power4(self):
        self.assertEqual(power(3,.5),1.7320508075688772)

    def test_power5(self):
        self.assertEqual(power(-3,3),-27)

    def test_power6(self):
        self.assertEqual(power(-1,-4),1)
    
    def test_power7(self):
        self.assertAlmostEqual(power(3,-1),0.333, delta= 0.001)
    
    def test_square_root(self):
        self.assertEqual(square_root(16),4)

    def test_square_root2(self):
        with self.assertRaises(ValueError):
            square_root(-9)


    def test_square_root3(self):
        self.assertEqual(square_root(1),1)

    def test_square_root4(self):
        self.assertEqual(square_root(100),10)

    def test_absolute_value(self):
        self.assertEqual(absolute_value(-10),10)

    def test_absolute_value2(self):
        self.assertEqual(absolute_value(100),100)

    def test_absolute_value3(self):
        self.assertEqual(absolute_value(-241),241)

    def test_absolute_value4(self):
        self.assertEqual(absolute_value(1),1)

    def test_mean(self):
        self.assertEqual(mean([1,2,3,4,5]),3)
    
    def test_mean2(self):
        self.assertEqual(mean([1,1,1,1]),1)

    def test_mean3(self):
        self.assertEqual(mean([0,0,1,0,-1]),0)

    def test_mean4(self):
        with self.assertRaises(ValueError):
            mean([])

    def test_mean5(self):
        with self.assertRaises(TypeError):
            mean(["h","e","l","l","o"])

    def test_median(self):
        self.assertEqual(median([1,3,5,7,9]),5)

    def test_median2(self):
        self.assertEqual(median([2,4,6,8]),5)

    def test_median3(self):
        with self.assertRaises(ValueError):
            median([])

    def test_median4(self):
        with self.assertRaises(TypeError):
            median([2,"s"])

    def test_mode(self):
        self.assertEqual(mode([1,2,2,3,4]),2)

    def test_mode2(self):
        self.assertEqual(mode([5,5,5,1,1,2,2]),5)

    def test_mode3(self):
        with self.assertRaises(ValueError):
            mode([])

    def test_variance(self):
        self.assertAlmostEqual(variance([1,2,3,4,5]), 2.0)

    def test_variance2(self):
        self.assertAlmostEqual(variance([1,1,1,1,1,1,1,1,1,1,1]), 0)

    def test_variance3(self):
        with self.assertRaises(ValueError):
            variance([])

    def test_standard_deviation(self):
        self.assertAlmostEqual(standard_deviation([1,2,3,4,5]), 1.4142135623730951)

    def test_standard_deviation2(self):
        self.assertAlmostEqual(standard_deviation([0,0,0,0,-1]), 0.4472135954999579, delta=0.1)

    def test_standard_deviation3(self):
        self.assertAlmostEqual(standard_deviation([-1,-2,-3,-4,-5]), 1.4142135623730951)

    def test_standard_deviation4(self):
        with self.assertRaises(ValueError):
            standard_deviation([])

    def test_is_even(self):
        self.assertTrue(is_even(10))

    def test_is_even2(self):
        self.assertFalse(is_even(7))

    def test_is_even3(self):
        self.assertTrue(is_even(0))

    def test_is_even4(self):
        self.assertTrue(is_even(-4))

    def test_is_prime(self):
        self.assertTrue(is_prime(13))

    def test_is_prime(self):
        self.assertTrue(is_prime(13))

    def test_is_prime2(self):
        self.assertFalse(is_prime(10))

    def test_is_prime3(self):
        self.assertFalse(is_prime(1))

    def test_is_prime4(self):
        self.assertTrue(is_prime(2))

    def test_is_prime5(self):
        self.assertEqual(is_prime(25), False)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial2(self):
        self.assertEqual(factorial(0),1)

    def test_factorial3(self):
        with self.assertRaises(ValueError):
            factorial(-3)

    def test_factorial4(self):
        self.assertEqual(factorial(1),1)

    def test_factorial5(self):
        self.assertEqual(factorial(6),720)

    def test_factorial6(self):
        self.assertEqual(factorial(3),6)

    def test_gcd(self):
        self.assertEqual(gcd(54,24),6)

    def test_gcd2(self):
        self.assertEqual(gcd(101,10),1)
    
    def test_gcd3(self):
        self.assertEqual(gcd(0,5),5)

    def test_gcd4(self):
        self.assertEqual(gcd(0,0),0)

    def test_gcd5(self):
        self.assertEqual(gcd(56,98),14)

    def test_gcd6(self):
        self.assertEqual(gcd(7,3),1)


if __name__ == '__main__':
    unittest.main(verbosity=2)