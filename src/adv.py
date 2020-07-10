
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons",
                    [Item("cave water", "tasting cave water to quench your thirst"), 
                    Item("cave mushroom", "this cave mushroom has an unusual look..."), 
                    Item("cave Moss", "Looks slightly more appetizing than the mushroom")]),

    'foyer':    Room("Foyer", 
                    "Dim light filters in from the south. Dusty passages run north and east.",
                    [Item( "foyer pillow", "this pillow is more uncomfortable than it looks"), 
                    Item("flower vase", "the nice vase to put flowers in"), 
                    Item("furniture piece", "A nice Victorian furnicture piece that one can sit on")]),
                

    'overlook': Room("Grand Overlook", 
                    "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.",
                    [Item("Shiny Rock", "The most shiniest rock you've ever seen in your life"),
                    Item("Candy wrapper", "reese's pieces candy wrapper."),
                    Item("binoculars", "an old pair of binoculars that seem to still work")]),

    'narrow':   Room("Narrow Passage", 
                    "The narrow passage bends here from west to north. The smell of gold permeates the air.",
                    [Item("Flashlight", "a flashlight! Hopefully this will be usefull"), 
                    Item("HydroFlask", "Someone seemed to leave their HydroFlask here"),
                    Item("Map", "A map with details of a treasure near by")]),

    'treasure': Room("Treasure Chamber", 
                    "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.",
                    [Item("Gold Coin", "a single gold coin glimmers at the edge the room"),
                    Item("The Lengendary Sword Excalibar", "The Lengendary Sword is fitted onto this golden rock, only the chosen one can lift the sword from the stone"),
                    Item("treasure note", "Note reads: haha beat ya to it!")]),
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
    print(f"Items: \n 1) {playerOne.room.items[0]} \n 2) {playerOne.room.items[1]} \n 3) {playerOne.room.items[2]}")
    
    print()


    playerChoice = input("Instructions: \n To travel type: s , n , w , e.  or q to quit: \n To pick up an item type in the corresponding number: \n")

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

