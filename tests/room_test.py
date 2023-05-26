import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song
from classes.drink import Drink

class TestRoom(unittest.TestCase):
    def setUp(self):
        song_1 = Song("Love Shack", "The B52s")
        song_2 = Song("Rock Lobster", "The B52s")
        song_3 = Song("Planet Claire", "The B52s")
        playlist = [song_1, song_2, song_3]
        self.room = Room(playlist, 10, 10.00,) 
    
    def test_room_has_playlist(self):
        self.assertEqual(3, len(self.room.playlist))

    def test_room_has_capacity(self):
        self.assertEqual(10, self.room.capacity)

    def test_room_has_entry_fee(self):
        self.assertEqual(10.00, self.room.entry_fee)

    def test_room_has_no_guests(self):
        self.assertEqual(0, len(self.room.guests))

    def test_room_has_empty_till(self):
        self.assertEqual(0, self.room.till)

    def test_add_song(self):
        new_song = Song("Battery", "Metallica")
        self.room.add_song(new_song)
        self.assertEqual(4, len(self.room.playlist))