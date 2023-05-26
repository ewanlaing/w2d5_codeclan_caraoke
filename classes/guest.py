class Guest:
    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song

    def check_in(self, room):
        if len(room.guests) + 1 <= room.capacity:
            if self.wallet >= room.entry_fee:
                room.guests.append(self)
                room.till += room.entry_fee

    def check_out(self, room):
        if self in room.guests:
            room.guests.remove(self)

    def found_favourite(self, room):
        for song in room.playlist:
            if self.favourite_song == song.name:
                return "Whoo!"
        return None
    
    def order_drink(self, room, drink):
        if self.wallet >= drink.price:
            self.wallet -= drink.price
            room.till += drink.price

    def add_time(self, room, number_of_hours):
        cost = number_of_hours * 5
        if self. wallet >= cost:
            self.wallet -= cost
            room.till += cost