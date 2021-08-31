from player_object import Player_Object

players = list()
complete_list = False
while not (complete_list):
    enter_new_player = input("Enter new player? y/n :")
    if enter_new_player == "y" or enter_new_player == "Y":
        #new_player = Player_Object()
        new_in = input("Please enter a new player (name hp ac str dex con wis int cha) :")

        if new_in == '':
            stat_list = ["Default"]
        else:
            stat_list = new_in.split()
        
        if len(stat_list) != 9:
            stat_length = len(stat_list)
            while stat_length < 9:
                stat_list.append(10)
                stat_length += 1

        new_player = Player_Object(
            stat_list[0],
            stat_list[1],
            stat_list[2],
            stat_list[3],
            stat_list[4],
            stat_list[5],
            stat_list[6],
            stat_list[7],
            stat_list[8]
            )
        """
        x = [None] * 9
        i = 0
        for stat in new_in:
            x[i] = new_in[i]
            i += 1
        new_player.name = x[0]
        new_player.hp = x[1]
        new_player.ac = x[2]
        new_player.str = x[3]
        new_player.dex = x[4]
        new_player.con = x[5]
        new_player.wis = x[6]
        new_player.intel = x[7]
        new_player.chari = x[8]
        """

        players.append(new_player)
        print("You have added " + players[-1].name)
    else:
        print("You have chosen to stop entering new players.")
        print("This is the current list of players : ")
        for player in players:
            player.show_stats()
        break