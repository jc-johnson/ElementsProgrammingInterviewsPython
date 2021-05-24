import unittest
import PrimitiveTypes

class TestPrimitiveTypes(unittest.TestCase):

    def test_Count_Bits(self):
        self.assertEqual(PrimitiveTypes.count_bits(1101), 15)
        self.assertEqual(PrimitiveTypes.count_bits(1111), 6)

if __name__ == '__main__':
    unittest.main()
