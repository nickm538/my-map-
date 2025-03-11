import unittest
from src.utils.map_utils import render_map, place_pin

class TestMapUtils(unittest.TestCase):

    def test_render_map(self):
        # Test rendering of the static map
        map_image = render_map()
        self.assertIsNotNone(map_image)
        self.assertTrue(map_image.endswith('.png'))  # Assuming the map is saved as a PNG file

    def test_place_pin(self):
        # Test placing a pin on the map
        pin_location = (40.789142, -73.134960)  # Example coordinates for Long Island
        pin_details = "Encountered a homeless person"
        result = place_pin(pin_location, pin_details)
        self.assertTrue(result)
        self.assertIn(pin_details, result)  # Assuming the result contains the pin details

if __name__ == '__main__':
    unittest.main()