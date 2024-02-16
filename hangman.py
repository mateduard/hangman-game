from game_functions import getWord, play, getPlayAgain

playAgainFlag = 1
while (playAgainFlag):
    chosenWord = getWord()
    play(chosenWord)
    playAgainFlag = getPlayAgain()
