import colorama
import os

clear = lambda: os.system("cls")
colorama.init()

white_color = colorama.Fore.WHITE
green_color = colorama.Fore.GREEN
red_color = colorama.Fore.RED
blue_color = colorama.Fore.BLUE

board = list(range(0, 9))
cells = 3
dashes = 13

spaces = 14
counter = 0
is_win = False
win_coords = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

player_token = ""

print(green_color + "Tic-Tac toe the game")

def draw_board():
    for i in range(cells):
        print(blue_color + " " * spaces, end="")
        print(blue_color + "-" * dashes)
        print(" " * spaces, end="")
        print(
            f"{blue_color}| {white_color}{board[0 + i * 3]} {blue_color}| {white_color}{board[1 + i * 3]} {blue_color}| {white_color}{board[2 + i * 3]} {blue_color}|")
        print(" " * spaces, end="")
        print(blue_color + "-" * dashes)


while not is_win:
    draw_board()

    if counter % 2 == 0:
        player_token = "X"
    else:
        player_token = "0"

    is_valid = False
    while not is_valid:
        player_answer = input(f"{white_color}Where we put a {player_token}?:")
        try:
            player_answer = int(player_answer)
        except:
            print(red_color + "Invalid input. A niumber excepted")
            continue
        if 0 <= player_answer <= 8:
            if str(board[player_answer]) not in "XD":
                board[player_answer] = player_token
                is_valid = True
            else:
                print(red_color + "this cell is already taken!")
                continue
        clear()
        counter += 1

        if counter > 4:
            for each in win_coords:
                if board[each[0]] == board[each[1]] == board[each[2]]:
                    is_win = True
                    break
                if is_win:
                    print(f"{green_color}{player_token} is win")
                    break
            if counter == 9:
                print(green_color + "Draw! You re amazibg")
                break

        if counter == 9:
            print(green_color + "Draw! Yore amazing")
            break

draw_board()

input(white_color + "opress the enter to exit")

