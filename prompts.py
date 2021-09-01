class Prompts:

    def what_do():
        '''Asks user for action'''
        return input("What would you like to do? : ")
    
    def player_list_manipulate():
        '''Asks what you would like to manipulate in the list of players'''
        return input("Create, Read, Update, Delete Players, Finish Modifying or Exit program :").upper()
    
    def player_create():
        '''Asks for the values to put into the new player'''
        return input("Please enter a new player (name hp ac str dex con wis int cha) :")
    
    def player_create_success(player):
        '''Lets user know that the new player has been added successfully'''
        return print("You have added " + player)
    
    def player_access():
        '''Asks the user which player they would like to access'''
        return int(input("Enter the index of the player to access : "))
    
    def current_players():
        '''Displays the current list of players'''
        return print("This is the current list of players : ")
    
    def no_players():
        '''Lets the user know that the list of players is empty'''
        return print("There are no players to display.")