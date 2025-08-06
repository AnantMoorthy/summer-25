# Project No.: 3
# Author: Anant Moorthy
# Description: Program generates a boggle board based on a given seed value. User enters a word, program crosscheck the word with the board and checks if the word is a palindrome. States if word is or not valid and/or a palindrome. Prints out the board with the valid word highlighted letter by letter.

from boggle_board import BoggleBoard

def main():
    try:
        seed = int(input("Enter seed: "))
    except ValueError:
        print("Invalid seed")
        return

    boggle = BoggleBoard(seed)
    boggle.printBoard()

    word = input("Enter a word (in UPPERcase) : ").upper()

    found  = boggle.isValidWord(word)
    if found:
        print("Nice Job!")
        if boggle.checkPalin(word):
            print("The word " + word + " is a palindrome.")
        else:
            print("The word " + word + " is not a palindrome.")
        boggle.printBoardWord()
    else:
        print("I don't see that word.")
        if boggle.checkPalin(word):
            print("The word " + word + " is a palindrome.")
        else:
            print("The word " + word + " is not a palindrome.")
            print("Are we looking at the same board?")


main()