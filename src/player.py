# Write a class to hold player information, e.g. what room they are in
# currently.


class Player: 
    def __init__(self, id, name, room, items = []):
        self.id = id 
        self.name = name
        self.room = room
        self.items = items
    
    def __str__(self):
        return f"currently in {self.room}"