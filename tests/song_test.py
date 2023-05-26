import unittest
from classes.song import Song
from classes.guest import Guest
from classes.room import Room
from classes.drink import Drink

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Love Shack", "The B52s")

    def test_song_has_name(self):
        self.assertEqual("Love Shack", self.song.name)

    def test_song_has_artist(self):
        self.assertEqual("The B52s", self.song.artist)