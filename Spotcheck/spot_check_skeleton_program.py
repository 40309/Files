class game():
    def __init__(self):
        self.name = None
        self.plaform = None
        self.genre = None
        self.cost = None
        self.number_of_players = None
        self.online_functionality = None


def load_games(filename):
    pass

def save_games(filename, games):
    pass

#the parameter is games because eventually you will be displaying
#multiple games using this function
def display_games(games):
    for count in range(len(games)):
        for count_2 in range(1):
            print("Name: {0}".format(games[count-1][count_2-1]))
            print("Platform: {0}".format(games[count-1][count_2]))
            print("Genre: {0}".format(games[count-1][count_2+1]))
            print("Cost: {0}".format(games[count-1][count_2+2]))
            print("Number of Players: {0}".format(games[count-1][count_2+3]))
            print("Online Functionality: {0}".format(games[count-1][count_2+4]))
        
def get_game_from_user():
    games = []
    checker = False
    while checker == False:
        for count in range(1):
            temp = []
            game.name = input("Please enter the name of the game: ")
            if game.name == "-1":
                checker = True
                break
            
            game.plaform = input("Please enter the name of the plaform: ")
            game.genre = input("Please enter the name of genre of the game: ")
            game.cost = input("Please enter the cost of the game: ")
            game.number_of_players = int(input("Please enter the number of players: "))
            game.online_functionality = input("Does the game have Online Functionality? ")
            temp.append(game.name)
            temp.append(game.plaform)
            temp.append(game.genre)
            temp.append(game.cost)
            temp.append(game.number_of_players)
            temp.append(game.online_functionality)
        games.append(temp)
    return games
        
    

def display_menu():
    print()
    print("***Welcome to the Computer and Video Game Database***")
    print()
    print("1. Add new games")
    print("2. Display games")
    print("3. Exit program")
    print()

def main():
    exit_program = False
    while not exit_program:
        display_menu()
        selected_option = int(input("Please select a menu option: "))
        if selected_option == 1:
            games = get_game_from_user()
        elif selected_option == 2:
            display_games(games)
        elif selected_option == 3:
            pass
        else:
            print("Please enter a valid option (1-3)")
            print()

if __name__ == "__main__":
    main()
