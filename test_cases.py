#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        # 代表値5,50,500 境界値0, 1 ,999 ,1000 無効同値1500 ,500.1 ,-10 ,0.1 ,-0.1 ,a ,abc, ###, ５
        # 代表値のテスト
        def test_sample10 (self):
                self.assertEqual (250000, calc(500,500))

        # 境界値とのテスト
        def test_sample20 (self):
                self.assertEqual (500, calc(1,500))

        def test_sample21 (self):
                self.assertEqual (50, calc(50,1))

        def test_sample22 (self):
                self.assertEqual (-1, calc(0,500))

        def test_sample23 (self):
                self.assertEqual (-1, calc(5,0))

        def test_sample24 (self):
                self.assertEqual (4995, calc(999,5))

        def test_sample25 (self):
                self.assertEqual (49950, calc(50,999))

        def test_sample26 (self):
                self.assertEqual (-1, calc(1000,5))

        def test_sample27 (self):
                self.assertEqual (-1, calc(50,1000))

        def test_sample28 (self):
                self.assertEqual (999, calc(1,999))

        def test_sample28 (self):
                self.assertEqual (-1, calc(0,1000))

        # 無効同値のテスト
        def test_sample30 (self):
                self.assertEqual (-1, calc(5,1500))

        def test_sample31 (self):
                self.assertEqual (-1, calc(500.1,50))

        def test_sample32 (self):
                self.assertEqual (-1, calc(500,-10))

        def test_sample34 (self):
                self.assertEqual (-1, calc(0.1,5))

        def test_sample35 (self):
                self.assertEqual (-1, calc(500,-0.1))

        def test_sample36 (self):
                self.assertEqual (-1, calc('a',5))

        def test_sample37 (self):
                self.assertEqual (-1, calc(50,'abc'))