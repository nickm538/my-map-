import unittest
from src.services.location_service import save_pin, get_pins
from src.database.models import Pin

class TestLocationService(unittest.TestCase):

    def setUp(self):
        # Set up a test database or mock database
        self.test_pin = Pin(location="Test Location", details="Test details")

    def test_save_pin(self):
        result = save_pin(self.test_pin)
        self.assertTrue(result)
        # Add more assertions to verify the pin is saved correctly

    def test_get_pins(self):
        save_pin(self.test_pin)
        pins = get_pins()
        self.assertIn(self.test_pin, pins)

if __name__ == '__main__':
    unittest.main()