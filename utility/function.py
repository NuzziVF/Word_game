import os

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def create(alphabet):
    with open("dictionary/dict.txt", "r") as dic:
        l = dic.read().split()

        for alpha in alphabet:
            for letter in l:
                if letter[0] == alpha:
                    with open(f"dictionary/{alpha}.txt", "a") as text:
                        text.write(letter + "\n")


def delete(alphabet):
    for each in alphabet:
        os.remove("dictionary/" + each + ".txt")
