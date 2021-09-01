from player_class import Player
from npc_class import NPC

running = True
user_input = ''
def user_action():
    return input("What would you like to do? : ")

while running:
    #user_input = input("Welcome to Character Tracker.\nWhat would you like to do? : ")
    user_input = user_action()
    if user_input == "modify players":
        # Prompts user with the option to enter a new player
        user_input = input("Create, Read, Update, Delete Players or Exit program :").upper()

        # Initiates the input of a new player
        if user_input == "CREATE":
            player_input = input("Please enter a new player (name hp ac str dex con wis int cha) :")
            new_player = Player.add_new(player_input, Player.players)

            # Adds new player to the list and 
            # displays the most recently added player
            Player.players.append(new_player)
            print("You have added " + Player.players[-1].name)

        elif user_input == "READ":
            Player.show_players(Player.players)
            user_input = user_action()

        elif user_input == "UPDATE":
            pass

        # Deletes a player from the list of players
        elif user_input == "DELETE":
            print("This is the current list of players : ")
            for player in Player.players:
                print(Player.players.index(player))
                player.my_name()
            # Takes the index of the character the user wishes to delete
            player_remove = int(input("Enter the index of the player to remove : "))
            del Player.players[player_remove]
            user_input = user_action()

        else:
            # Completes the process of adding players to the list and
            # displays all players entered
            print("You have chosen to stop entering new players.")
            print("This is the current list of players : ")
            Player.show_players()
            print('')
            user_input = user_action()