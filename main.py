import random
import time, os, sys
from typing import List


def tPrintslow(text) -> None:
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.8)


def tPrintfast(text) -> None:
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)


def tInputslow(text) -> str:
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    value = input()
    return value


def tInputfast(text) -> str:
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    value = input()
    return value


def exposition() -> None:
    rules = """\nThe computer generates the first word,
You must type a word that starts with the last letter of the presented word,\n
(If Single Player)
The computer generates a new word starting with your last letter,
Game continues until either the computer runs out of words or you run out of words,\n
(if Local Player)
The game will ask for the next player to enter their word,
the game will also check the word for it to exist and start with the last letter,
The first to run out of words under 1 minute loses,
Time will gradually get shorter as the game goes on,\n"""
    tPrintfast("\n\nWelcome the word game. Here are the rules:")
    tPrintfast(rules)


def main_menu(l: List) -> str:
    hel = """\nSingle Player - Play against a bot that chooses words out of a large dictionary.\n
Local Player - Play against another person or group."""
    while True:
        choice = tInputslow("\n\nSingle Player\nLocal Player\nHelp\n> ").lower()
        if choice == "help":
            tPrintfast(hel)
        for each in l:
            if choice == each:
                return choice


def initial_word() -> str:
    with open("dictionary/dict.txt", "r") as file:
        computer = file.read().split()
        computer_choice = random.choice(computer)
        print(computer_choice)
        return computer_choice


def players_input(CC: str):
    p1 = input("> ")


def singleplayer_game():
    computer_choice = initial_word()


def localplayer_game():
    pass


def main() -> None:
    main_menu_choices = [
        "single player",
        "local player",
        "single",
        "singe",
        "local",
        "2",
        "1",
    ]
    single_choices = ["single player", "single", "singe", "1"]
    local_choices = ["local player", "local", "2"]
    try:
        exposition()
    except KeyboardInterrupt:
        pass
    choice = main_menu(main_menu_choices)
    for each in single_choices:
        if choice == each:
            singleplayer_game()
    for each in local_choices:
        if choice == each:
            localplayer_game()


if __name__ == "__main__":
    main()
