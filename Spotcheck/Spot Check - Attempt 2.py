import pickle

class game():
    def __init__(self):
        self.name = None
        self.platform = None
        self.genre = None
        self.cost = None
        self.number_of_players = None
        self.online_functionality = None
    

def load_games():
    try:
        with open("games.dat", mode="rb") as my_file:
            file_data = pickle.load(my_file)
            for line in file_data:
                print(line)
    except ValueError:
        print("The file requested does not exist")
    pass

def save_games(games):
    with open("games.dat",mode="wb") as my_file:
        pickle.dump(games,my_file)
    print("List has been Saved")
    print()
    pass

#the parameter is games because eventually you will be displaying
#multiple games using this function
def display_games(games):
    print()
    for count in range(len(games)):
        for each in range(1):
            print()
            print("Name: {0}".format(games[count-1][0]))
            print("Platform: {0}".format(games[count-1][1]))
            print("Genre: {0}".format(games[count-1][2]))
            print("Cost: {0}".format(games[count-1][3]))
            print("Number of Players: {0}".format(games[count-1][4]))
            print("Online Functionality: {0}".format(games[count-1][5]))
    pass

def get_game_from_user(games):
    checker = False
    while checker == False:
        print()
        temp = []
        game.name = input("Please enter the title of the game: ")
        if game.name == "-1":
            checker = True
            break
        game.platform = input("Please enter the name of the plaform: ")
        game.genre = input("Please enter the genre of the game: ")
        game.cost = input("Please enter the cost of the game: ")
        game.number_of_players = input("Please enter the number of players: ")
        game.online_functionality = input("Does the game have Online Functionality? ")
        temp.append(game.name)
        temp.append(game.platform)
        temp.append(game.genre)
        temp.append(game.cost)
        temp.append(game.number_of_players)
        temp.append(game.online_functionality)
        games.append(temp)
    return games
    pass

def display_menu():
    print()
    print("***Welcome to the Computer and Video Game Database***")
    print()
    print("1. Add new games")
    print("2. Display games")
    print("3. Save List of Games")
    print("4. Load List of Games")
    print("5. Exit program")
    print()

def main():
    games = []
    exit_program = False
    while not exit_program:
        display_menu()
        checker = False
        while checker == False:
            try:
                selected_option = int(input("Please select a menu option: "))
                checker = True
            except ValueError:
                print("Try Again, please")
        if selected_option == 1:
            games = get_game_from_user(games)
            pass
        elif selected_option == 2:
            display_games(games)
            pass
        elif selected_option == 3:
            save_games(games)
            exit_program = True
            pass
        elif selected_option == 4:
            load_games()
            pass
        elif selected_option == 5:
            exit_program = True
            pass
        else:
            print("Please enter a valid option (1-3)")
            print()

if __name__ == "__main__":
    main()
