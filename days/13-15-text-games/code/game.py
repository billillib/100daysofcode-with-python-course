import random


def main():
    print_header()
    ask_player_name()
    game_loop(create_rolls())


class Roll:

    def __init__(self, name):
        self.name = name
        self.beats = None
        self.loses = None

    def can_defeat(self, beats):
        if self.beats == beats:
            return True
        else:
            return False

    def loses_to(self, loses):
        if self.loses == loses:
            return True
        else:
            return False


def print_header():
    print("Welcome to the awesome game of ROCK PAPER SCISSORS!!!")


def ask_player_name():
    name = input("What is your name: ")
    continue_game = input(f'are you ready to rock {name}? Type YES or NO: ')
    if continue_game.upper() == 'YES':
        print('Heck YEA!')
    else:
        print(f'Bye {name}...')
        exit()


def create_rolls():
    paper = Roll('Paper')
    rock = Roll('Rock')
    scissors = Roll('Scissors')

    paper.beats = rock
    paper.loses = scissors

    rock.beats = scissors
    rock.loses = paper

    scissors.beats = paper
    scissors.loses = rock

    return paper, rock, scissors


def player_input(rolls):
    choice = input("[R]ock, [P]aper, [S]cissors: ")
    if choice.upper() == 'R':
        return rolls[1]
    elif choice.upper() == 'P':
        return rolls[0]
    elif choice.upper() == 'S':
        return rolls[2]
    else:
        print("Invalid input")


def computer_input(rolls):
    computer = random.choice(rolls)
    return computer


def game_action(player, computer):
    print(f'You chose {player.name}, computer chose {computer.name}')
    if player.can_defeat(computer):
        print('You won!')
        return 1
    elif player.loses_to(computer):
        print('You lost!')
        return 0
    else:
        print('Tie!')
        return -1


def game_loop(rolls):
    tracker = {'player': 0, 'computer': 0, 'tie': 0}
    count = 0
    while count < 3:
        computer_roll = computer_input(rolls)
        player_roll = player_input(rolls)

        outcome = game_action(player_roll, computer_roll)

        if outcome == 1:
            tracker["player"] += 1
        elif outcome == 0:
            tracker["computer"] += 1
        else:
            tracker["tie"] += 1

        count += 1
        # print(tracker)

    if tracker.get("player") > tracker.get("computer"):
        print("YOU WON THE WHOLE THING!")
    elif tracker.get("player") < tracker.get("computer"):
        print("YOU LOST TO A COMPUTER OMG")
    else:
        print("HOW DID YOU TIE THREE TIMES IN A ROW??!?")


if __name__ == '__main__':
    main()
