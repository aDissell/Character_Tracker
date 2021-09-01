from player_class import Player
from npc_class import NPC

players = list()
running = True

while running:
    action = input("Welcome to Character Tracker.\nWhat would you like to do? : ")
    if action == "modify players":
        # Prompts user with the option to enter a new player
        enter_new_player = input("Create, Remove, Update, Delete Players or Exit program :")

        # Initiates the input of a new player
        if enter_new_player == "Add" or enter_new_player == "add":
            player_input = input("Please enter a new player (name hp ac str dex con wis int cha) :")
            new_player = Player.add_new(player_input, players)

            # Adds new player to the list and 
            # displays the most recently added player
            players.append(new_player)
            print("You have added " + players[-1].name)

        elif enter_new_player == "Remove" or enter_new_player == "remove":
            pass
        
        elif enter_new_player == "Update" or enter_new_player == "update":
            pass

        elif enter_new_player == "Delete" or enter_new_player == "delete":
            pass

        else:
            # Completes the process of adding players to the list and
            # displays all players entered
            print("You have chosen to stop entering new players.")
            print("This is the current list of players : ")
            for player in players:
                player.my_name()
                player.my_hp()
            print('')
            action = input("What would you like to do? : ")


        running = False