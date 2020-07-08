# Write a class to hold player information, e.g. what room they are in
# currently.


class player: 
    def __init__(self, id, name):
        self.id = id 
        self.name = name
    
    def __str__(self):
        return f"{self.id}: {self.name}"