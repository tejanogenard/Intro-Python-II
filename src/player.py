# Write a class to hold player information, e.g. what room they are in
# currently.


class Player: 
    def __init__(self, id, name, room, items = []):
        self.id = id 
        self.name = name
        self.room = room
        self.items = items
    
    def add_to_inventory(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.pop(item)