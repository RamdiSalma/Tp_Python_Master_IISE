import unittest
from conversion import dollars_to_dirhams, meters_to_kilometers

class TestConversion(unittest.TestCase):

    def test_dollars_to_dirhams(self):
        """Test de conversion de dollars en dirhams."""
        self.assertEqual(dollars_to_dirhams(1), 10)
        self.assertEqual(dollars_to_dirhams(0), 0)
        self.assertEqual(dollars_to_dirhams(100), 1000)
        self.assertAlmostEqual(dollars_to_dirhams(12.5), 125)

    def test_meters_to_kilometers(self):
        """Test de conversion de mètres en kilomètres."""
       
        self.assertEqual(meters_to_kilometers(0), 0)
        self.assertEqual(meters_to_kilometers(500), 0.5)
        self.assertAlmostEqual(meters_to_kilometers(1234), 1.234)

if __name__ == "__main__":
    unittest.main()
