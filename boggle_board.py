# Project No.: 3
# Author: Anant Moorthy
# Description: Program generates a boggle board based on a given seed value. User enters a word, program crosscheck the word with the board and checks if the word is a palindrome. States if word is or not valid and/or a palindrome. Prints out the board with the valid word highlighted letter by letter.

import random
import string

class BoggleBoard:
    def __init__(self, seed):
        self.seed = seed
        random.seed(seed)
        self.bogBoard = []
        self.wordFound = []
        self.createBoard()

    def createBoard(self):
        self.bogBoard = [[random.choice(string.ascii_uppercase) for i in range(len(str(self.seed)))]for j in range(len(str(self.seed)))]

    def printBoard(self):
        for row in self.bogBoard:
            print("+---+ +---+ +---+ +---+")
            print(''.join("| " + letter + " | " for letter in row))
            print("+---+ +---+ +---+ +---+")

    def printBoardWord(self):
        for i, row in enumerate(self.bogBoard):
            print("+---+ +---+ +---+ +---+")
            for j, letter in enumerate(row):
                if (i,j) in self.wordFound:
                    print("|<" + letter + ">| ", end="")
                else:
                    print("| " + letter + " | ", end="")
            print()
        print("+---+ +---+ +---+ +---+")

    def isValidWord(self, word):
        if len(word) < 2 or len(word) > 5:
            return False


        for i in range(len(str(self.seed))):
            for j in range(len(str(self.seed))):
                if self.bogBoard[i][j] == word[0]:
                    visitAlr = [[False for i in range(len(str(self.seed)))] for j in range(len(str(self.seed)))]
                    path = []
                    if self.dfSearch(word, i, j, 0, visitAlr, path):
                        self.wordFound = path
                        return True
        return False

    def dfSearch(self, word, i, j, index, visitAlr, path):
        if index == len(word):
            return True

        if i < 0 or i >= len(str(self.seed)):
            return False
        elif j < 0 or j >= len(str(self.seed)):
            return False

        if visitAlr[i][j]:
            return False

        if self.bogBoard[i][j] != word[index]:
            return False
        visitAlr[i][j] = True
        path.append((i,j))

        paths = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for deltaRow, deltaCol in paths:
            if self.dfSearch(word, i + deltaRow, j + deltaCol, index + 1, visitAlr, path):
                return True

        visitAlr[i][j] = False
        path.pop()
        return False

    def checkPalin(self, word):
        if len(word) < 2:
            return True
        if word[0] != word[-1]:
            return False
        return self.checkPalin(word[1:-1])