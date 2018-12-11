def main():
    print_header()
    player = ask_player_name()


def print_header():
    print("Welcome to the awesome game of ROCK PAPER SCISSORS!!!")


def ask_player_name():
    name = input("What is your name: ")
    continue_game = input(f'are you ready to rock {name}? Type YES or NO: ')
    if continue_game == 'YES':
        print('Heck YEA!')
    else:
        print(f'Bye {name}...')
        exit()


if __name__ == '__main__':
    main()
