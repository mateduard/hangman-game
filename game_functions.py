import random
from words_list import words_list
from positions import man_positions


def getWord():
    word = random.choice(words_list)
    return word.upper()


def matchCompletion(word, wordCompletion, letter):
    wordToList = list(wordCompletion)
    for index in range(len(word)):
        if (word[index] == letter):
            wordToList[index] = letter
    return ''.join(wordToList)
# matchCompletion returns the new string after checking the correct input letters in the word


def play(word):
    # print(word)
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    tries = 6
    print('\n', f"      Word: {word_completion}")
    while guessed == False and tries > 0:
        letter = input("Letter: ").upper()
        if (letter not in guessed_letters):
            guessed_letters.append(letter)
        else:
            print("Letter already tried. Choose another.")
            continue
        if letter not in word:
            tries -= 1
            print(
                man_positions[tries], f"      Word: {word_completion}", f"      Guessed: {guessed_letters}", '\n')
            if tries <= 0:
                print(f"Game over. The word was {word}.")
                break
        else:
            word_completion = matchCompletion(word, word_completion, letter)
            print(f"      Word: {word_completion}",
                  f"      Guessed: {guessed_letters}", '\n')
            finishedFlag = 1
            for charac in word_completion:
                if (charac == "_"):
                    finishedFlag = 0
                    break
            if (finishedFlag):
                guessed = True
                print("Congratulations! You guessed it!")
                break
    return 0


def getPlayAgain():
    inp = input("Play again? (y/n):")
    while inp.lower() not in ['y', 'n']:
        print("Please enter y or n!")
        inp = input("Play again? (y/n):")
        print("input:", inp)
    if inp.lower() == 'y':
        return 1
    else:
        return 0
