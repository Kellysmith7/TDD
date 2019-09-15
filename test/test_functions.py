import unittest
from main import camper_age_input


class FunctionTestCase(unittest.TestCase):
    def test_convert_age_months(self):
        self.assertEqual(camper_age_input.convert_to_months(-1),12)


if __name__ == '__main__':
    unittest.main()
