import unittest
import PrimitiveTypes

class TestPrimitiveTypes(unittest.TestCase):

    def test_Count_Bits(self):
        self.assertEqual(PrimitiveTypes.count_bits(11), 15)

if __name__ == '__main__':
    unittest.main()
