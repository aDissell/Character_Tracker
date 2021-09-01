from mob_class import Mob


class Player(Mob):
    players = list()
    def __init__(self, name, hp, ac, stren, dex, con, wis, intel, chari):
        super().__init__(name=name, hp=hp, ac=ac, stren=stren, dex=dex, con=con, wis=wis, intel=intel, chari=chari)

    def add_new(new_in, players):
        '''Takes a set of attributes and builds a new player
            returns a filled player object'''
        # Checks to see if the user entered anything to the console
        # if not, sets the first item in the list to a default name
        if new_in == '':
            stat_list = [("Default" + str(len(players)))]
        else:
            stat_list = new_in.split()
        
        # Checks to make sure the list contains all required inputs
        # if not, adds a a default input until all fields are filled
        if len(stat_list) != 9:
            stat_length = len(stat_list)
            while stat_length < 9:
                stat_list.append(10)
                stat_length += 1

        # Populates the new player object with
        # the stat list
        new_player = Player(
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
        return new_player