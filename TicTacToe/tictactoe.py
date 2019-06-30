import itertools

def all_same(l):
    if l.count(l[0]) == len(l) and l[0] != 0:
        return True
    else:
        return False
        
def win(current_game):
    #Horizontal Winner
    for row in current_game:
        #Counts the occurences of a number in a current row and checks if it is equal to the length of the row
        if all_same(row):
            print(f"Player {row[0]} wins horizontally")
            return True

    #Vertical Winner
    #iterate through the column index in the current game
    for col in range(len(current_game)):
        #Stores the values of a column
        check = [] 
        #iterates through the row index in the current game
        for row in current_game:
            #Appends the current value to check variable
            check.append(row[col])
        #Checks if there is a vertical winner
        if all_same(check):
            print(f"Player {check[0]} wins horizontally")
            return True

    #Diagonal Winner
    diags = []
    for i in range(len(current_game)):
        diags.append(current_game[i][i])
    if all_same(diags):
        print(f"Player {diags[0]} wins diagonally")
        return True

    #Reversed Diagonal
    diags = []
    for col, row in enumerate(reversed(range(len(current_game)))):
        diags.append(current_game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} wins diagonally")
        return True

    return False




def game_board(game, player = 0, row = 0, col = 0, just_display = False):

    try:
        if game[row][col] != 0:
            print ("Sorry, this position is occupied!")
            return game, False
        print("   0  1  2")
        if not just_display:
            game[row][col] = player
        for count, row in enumerate(game):
            print(count, row)
        return game, True

    except IndexError as e:
        print("Input column/row as 0 1 and 2 only", e)
        return game, False

    except Exception as e:
        print("Ooops something went wrong!", e)
        return game, False


playing = True
players = [1,2]

while playing:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle(players)

    while not game_won:
        current_player = next(player_choice)
        print (f"Current player: {current_player}")
        played = False

        while not played:
            try:
                column_choice = int(input("What column do you want to play?: "))
                row_choice = int(input("What row do you want to play?: "))
            except Exception as e:
                print("Please restart the game. Something went wrong to your input: ", e)

            game, played = game_board(game,current_player, row_choice,column_choice)

        if win(game):
            game_won = True
            playAgain = str(input("Do you want to play again?(y/n): "))
            if  playAgain.lower() == "y":
                print("Restarting the game......... Please wait")
            elif playAgain.lower() == "n":
                print("See you again...")
                playing = False
            else:
                print("Wrong input, bye")
                playing = False
 














