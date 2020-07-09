
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                    [Item( "cave water", "tasting cave water to quench your thirst"), 
                    Item("cave mushroom", "this cave mushroom has an unusual look...")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# Write a loop that:
# *print(playerOne.room.n_to)
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# Create play choice conditional 
# * how will the user move through the rooms. 
# * User will type s => south, n => north, w => west, e => east prompting to move 
# * the user into the appropriate room. 
# * - use if or else conditionals 
#   if user choice is x-direction  
# If the user enters "q", quit the game.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.


playerOne = Player(1, "playerOne", room['outside'])

while True:

    print()
    print(f"Location: {playerOne.room.name}")
    print(f"text: {playerOne.room.description}")
    print(f"Items:\n{playerOne.room.items[0]}\n{playerOne.room.items[1]}")
    
    print()

    playerChoice = input("To travel in a direction type: s , n , w , e.  or q to quit: ")

    if playerChoice == 'q':

        break
    elif playerChoice == 'w':
        if hasattr(playerOne.room, 'w_to'):
            playerOne.room = playerOne.room.w_to
        else:
            print("text: You cannot travel in that direction\n")

    elif playerChoice == 'n':
        if hasattr(playerOne.room, 'n_to'):
            playerOne.room = playerOne.room.n_to
        else:
            print("text: You cannot travel in that direction\n")
          
    elif playerChoice == 'e':
        if hasattr(playerOne.room, 'e_to'):
            playerOne.room = playerOne.room.e_to
        else:
            print("text: You cannot travel in that direction\n")
    
    elif playerChoice == 's':
        if hasattr(playerOne.room, 's_to'):
            playerOne.room = playerOne.room.s_to
        else:
            print("text: You cannot travel in that direction\n")

