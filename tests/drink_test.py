import unittest
from classes.song import Song
from classes.guest import Guest
from classes.room import Room
from classes.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("beer", 5.00)

    def test_drink_has_name(self):
        self.assertEqual("beer", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(5.00, self.drink.price)