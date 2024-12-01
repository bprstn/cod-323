import unittest
from city_functions import city_country  # Import the function to test

class TestCityCountry(unittest.TestCase):
    """Tests for the city_country function."""

    def test_city_country(self):
        """Does the function return a properly formatted string?"""
        # Test with only city and country
        result = city_country("Santiago", "Chile")
        self.assertEqual(result, "Santiago, Chile")

        # Test with city, country, and population
        result = city_country("Paris", "France", population=12000000)
        self.assertEqual(result, "Paris, France - population 12000000")

        # Test with city, country, population, and language
        result = city_country("Tokyo", "Japan", population=14000000, language="Japanese")
        self.assertEqual(result, "Tokyo, Japan - population 14000000, language Japanese")

if __name__ == "__main__":
    unittest.main()

