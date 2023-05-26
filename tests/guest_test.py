import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.drink import Drink

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Ewan", 100.00, "Love Shack")

    def test_guest_has_name(self):
        self.assertEqual("Ewan", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(100.00, self.guest.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Love Shack", self.guest.favourite_song)

    def test_guest_can_check_into_room(self):
        song_1 = Song("Love Shack", "The B52s")
        song_2 = Song("Rock Lobster", "The B52s")
        song_3 = Song("Planet Claire", "The B52s")
        playlist = [song_1, song_2, song_3]
        room = Room(playlist, 10, 10.00)
        self.guest.check_in(room)
        self.assertEqual(True, self.guest in room.guests)
        self.assertEqual(10.00, room.till) 

    def test_guest_cannot_check_in_capacity_full(self):
        song_1 = Song("Love Shack", "The B52s")
        song_2 = Song("Rock Lobster", "The B52s")
        song_3 = Song("Planet Claire", "The B52s")
        playlist = [song_1, song_2, song_3]
        room = Room(playlist, 1, 10.00)
        guest_2 = Guest("Sarah", 50.00, "Yellow")
        guest_2.check_in(room)
        self.guest.check_in(room)
        self.assertEqual(False, self.guest in room.guests)

    def test_guest_cannot_check_in_money(self):
        song_1 = Song("Love Shack", "The B52s")
        song_2 = Song("Rock Lobster", "The B52s")
        song_3 = Song("Planet Claire", "The B52s")
        playlist = [song_1, song_2, song_3]
        room = Room(playlist, 1, 110.00)
        self.guest.check_in(room)
        self.assertEqual(False, self.guest in room.guests)

    def test_guest_can_check_out(self):
        song_1 = Song("Love Shack", "The B52s")
        song_2 = Song("Rock Lobster", "The B52s")
        song_3 = Song("Planet Claire", "The B52s")
        playlist = [song_1, song_2, song_3]
        room = Room(playlist, 1, 10.00)
        room.guests.append(self.guest)
        self.guest.check_out(room)
        self.assertEqual(False, self.guest in room.guests)

    def test_found_favourite_song(self):
        song_1 = Song("Love Shack", "The B52s")
        song_2 = Song("Rock Lobster", "The B52s")
        song_3 = Song("Planet Claire", "The B52s")
        playlist = [song_1, song_2, song_3]
        room = Room(playlist, 1, 10.00)
        self.assertEqual("Whoo!", self.guest.found_favourite(room))

    def test_not_found_favourite_song(self):
        song_1 = Song("Daysleeper", "REM")
        song_2 = Song("Rock Lobster", "The B52s")
        song_3 = Song("Planet Claire", "The B52s")
        playlist = [song_1, song_2, song_3]
        room = Room(playlist, 1, 10.00)
        self.assertEqual(None, self.guest.found_favourite(room))

    def test_order_drink(self):
        song_1 = Song("Love Shack", "The B52s")
        song_2 = Song("Rock Lobster", "The B52s")
        song_3 = Song("Planet Claire", "The B52s")
        playlist = [song_1, song_2, song_3]
        room = Room(playlist, 1, 10.00)
        drink = Drink("beer", 5.00)
        self.guest.order_drink(room, drink)
        self.assertEqual(95.00, self.guest.wallet)
        self.assertEqual(5.00, room.till)

    def test_order_drink_too_expensive(self):
        song_1 = Song("Love Shack", "The B52s")
        song_2 = Song("Rock Lobster", "The B52s")
        song_3 = Song("Planet Claire", "The B52s")
        playlist = [song_1, song_2, song_3]
        room = Room(playlist, 1, 10.00)
        drink = Drink("beer", 500.00)
        self.guest.order_drink(room, drink)
        self.assertEqual(100.00, self.guest.wallet)
        self.assertEqual(0.00, room.till)

    def test_add_time(self):
        song_1 = Song("Love Shack", "The B52s")
        song_2 = Song("Rock Lobster", "The B52s")
        song_3 = Song("Planet Claire", "The B52s")
        playlist = [song_1, song_2, song_3]
        room = Room(playlist, 1, 10.00)
        self.guest.add_time(room, 1)
        self.assertEqual(95.00, self.guest.wallet)
        self.assertEqual(5.00, room.till)

    def test_add_time_cannot_afford(self):
        song_1 = Song("Love Shack", "The B52s")
        song_2 = Song("Rock Lobster", "The B52s")
        song_3 = Song("Planet Claire", "The B52s")
        playlist = [song_1, song_2, song_3]
        room = Room(playlist, 1, 10.00)
        self.guest.add_time(room, 200)
        self.assertEqual(100.00, self.guest.wallet)
        self.assertEqual(0.00, room.till)
        


    


        