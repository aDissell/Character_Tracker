from player_class import Player
from npc_class import NPC

#players = list()
running = True

while running:
    action = input("Welcome to Character Tracker.\nWhat would you like to do? : ")
    if action == "modify players":
        # Prompts user with the option to enter a new player
        enter_new_player = input("Create, Remove, Update, Delete, Display Players or Exit program :").upper()

        # Initiates the input of a new player
        if enter_new_player == "CREATE"
            player_input = input("Please enter a new player (name hp ac str dex con wis int cha) :")
            new_player = Player.add_new(player_input, Player.players)

            # Adds new player to the list and 
            # displays the most recently added player
            Player.players.append(new_player)
            print("You have added " + Player.players[-1].name)

        elif enter_new_player == "REMOVE":
            print("This is the current list of players : ")
            for player in Player.players:
                print(Player.players.index(player))
                player.my_name()
            player_remove = int(input("Enter the index of the player to remove : "))
            del Player.players[player_remove]

        elif enter_new_player == "UPDATE":
            pass

        elif enter_new_player == "DELETE":
            pass

        else:
            # Completes the process of adding players to the list and
            # displays all players entered
            print("You have chosen to stop entering new players.")
            print("This is the current list of players : ")
            for player in Player.players:
                player.my_name()
                player.my_hp()
            print('')
            action = input("What would you like to do? : ")