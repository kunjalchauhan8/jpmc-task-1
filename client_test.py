import unittest
from client import getRatio


class TestClient ( unittest.TestCase ) :
    def test_division_zero(self) :
        passed = self.assertIsNone ( getRatio ( 118.24, 0 ) ) == None
        if passed :
            print ( '[PASS] GetRatio - Divide By Zero' )
        else :
            print ( '[FAIL] GetRatio - Divide By Zero' )

    def test_stock_value(self) :
        passed = self.assertEqual ( getRatio ( 141.11, 132.94 ), 1.0614562960734166 ) == None
        if passed :
            print ( '[PASS] GetRatio - Normal Case' )
        else :
            print ( '[FAIL] GetRatio - Normal Case' )