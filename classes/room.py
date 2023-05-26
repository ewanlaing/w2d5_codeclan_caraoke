class Room:
    def __init__(self, playlist, capacity, entry_fee):
        self.playlist = playlist
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.guests = []
        self.till = 0.00

    def add_song(self, new_song):
        self.playlist.append(new_song)