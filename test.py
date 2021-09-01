from player_class import Player
from npc_class import NPC
from prompts import Prompts

running = True
user_input = ''

while running:
    #user_input = input("Welcome to Character Tracker.\nWhat would you like to do? : ")
    user_input = Prompts.what_do().upper()
    if user_input == "MODIFY PLAYERS":
        # Prompts user with the option to enter a new player
        user_input = Prompts.player_list_manipulate()

        # Initiates the input of a new player
        if user_input == "CREATE":
            player_input = Prompts.player_create()
            new_player = Player.player_create(player_input, Player.players)

            # Adds new player to the list and 
            # displays the most recently added player
            Player.players.append(new_player)
            Prompts.player_create_success(Player.players[-1].name)
            
        # Displays the current list of players
        elif user_input == "READ":
            Player.show_players(Player.players)

        #TODO: Add UPDATE functionality
        elif user_input == "UPDATE":
            Prompts.current_players()
            Player.show_players(Player.players)
            player_to_update = Player.players[Prompts.player_access()]
            what_update = input("What would you like to modify about " + player_to_update.my_name() + "?").upper()
            if what_update == "NAME":
                pass
            elif what_update == "HP":
                pass
            elif what_update == "AC":
                pass
            elif what_update == "STR":
                pass
            elif what_update == "DEX":
                pass
            elif what_update == "CON":
                pass
            elif what_update == "WIS":
                pass
            elif what_update == "INT":
                pass
            elif what_update == "CHA":
                pass
            else:
                print("You did not update any attributes for " + player_to_update.my_name() + ".")

        # Deletes a player from the list of players
        elif user_input == "DELETE":
            Prompts.current_players()
            Player.show_players(Player.players)
            # Takes the index of the character the user wishes to delete
            del Player.players[Prompts.player_access()]
        
        #TODO: Add ability to stop modifying player list
        elif user_input == "FINISH":
            pass

        else:
            # Completes the process of adding players to the list and
            # displays all players entered
            print("You have chosen to stop entering new players.")
            Prompts.current_players()
            Player.show_players()
            print('')
            user_input = Prompts.what_do()