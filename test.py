from player_class import Player
from npc_class import NPC

players = list()
leave_program = False

while not leave_program:
    # Prompts user with the option to enter a new player
    enter_new_player = input("Enter new player? y/n :")

    # Initiates the input of a new player
    if enter_new_player == "y" or enter_new_player == "Y":
        player_input = input("Please enter a new player (name hp ac str dex con wis int cha) :")
        new_player = Player.add_new(player_input, players)

        # Adds new player to the list and 
        # displays the most recently added player
        players.append(new_player)
        print("You have added " + players[-1].name)
        
    # Completes the process of adding players to the list and
    # displays all players entered
    else:
        print("You have chosen to stop entering new players.")
        print("This is the current list of players : ")
        for player in players:
            player.my_name()
            player.my_hp()
            print('')
        break