# Step one
ask user for an input: Start menu
opt 1
single player (aka bot)
opt 2 
Local Player (aka more than one user)

# Step two
phase two of start menu

if user chose single player:
    present a random word from dictionary
    must input a work starting with the last letter of the word
    bot chooses a random number from 0-101 and that decides chance to miss fire.
    if there is no misfire, use random choice to pick from the dictionary starting with the last letter of the input
    Repeat steps but keep increasing the chance at misfire

if user choses Local Player:
    user inputs the number of players
    choose a random word from the dictionary
    user must input work starting with the last letter
    the game checks to see if the word exists
    the text then asks the next player to input a word
    game checks to see if word is valid and starts right
    repeat

# Step three
Start thinking about how to make a save state that saved the words used and keeps track of the players position.