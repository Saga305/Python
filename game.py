"""
Implement Tic Tac Toe.
Application choose the random between the player and the computer to starts the game.
"""
import random as choose
import copy

class TictocToe:
    def __init__(self):
        self.playerLetter = None
        self.computerLetter = None
        self.board = [i for i in range(9,0,-1)]
        self.turn = choose.choice(["player","computer"])
        print("Wel Come to Tic Tac Toe...!!!")
        self.getPlayerLetter()
        print(f"{self.turn} will start first.")
        self.letsplay()

    def toggleTurn(self):
        """
        Toggle the Turn.
        :return: Nothing
        """
        if self.turn == "player":
            self.turn = "computer"
        else:
            self.turn = "player"

    def printBoard(self):
        """
        This function will print the board on the console.
        :return: Nothing
        """
        print("-------------")
        print("| {0} | {1} | {2} |".format(self.board[0],self.board[1],self.board[2]))
        print("-------------")
        print("| {0} | {1} | {2} |".format(self.board[3], self.board[4], self.board[5]))
        print("-------------")
        print("| {0} | {1} | {2} |".format(self.board[6], self.board[7], self.board[8]))
        print("-------------")

    def isWinner(self,board,letter):
        """
        Check the winning of the given letter into given self.board.
        :param board:
        :param letter:
        :return: Boolean
        """
        if ((board[0] == letter and board[1] == letter and board[2] == letter) or
                (board[3] == letter and board[4] == letter and board[5] == letter) or
                (board[6] == letter and board[7] == letter and board[8] == letter) or
                (board[0] == letter and board[3] == letter and board[6] == letter) or
                (board[1] == letter and board[4] == letter and board[7] == letter) or
                (board[2] == letter and board[5] == letter and board[8] == letter) or
                (board[0] == letter and board[4] == letter and board[8] == letter) or
                (board[2] == letter and board[4] == letter and board[6] == letter)):
            return True
        return False

    def getPlayerLetter(self):
        """
        The function asks player to choose the letter.
        """
        while self.playerLetter not in ('X', 'O'):
            self.playerLetter = input("Choose your letter, X or O?").upper()

        if self.playerLetter == 'X':
           self.computerLetter = 'O'
        else:
           self.computerLetter = 'X'

    def isSpaceavailable(self,board,move):
        """
        Check the given move is occupied into board or not.
        :param board:
        :param move:
        :return: Boolean
        """
        return (move in board)

    def getMovementFromPlayer(self):
        """
        take the move from the user.
        :return: integer
        """
        move = 0
        while move not in self.board:
            try:
                move = int(input("What is your next move(1-9)?"))
            except ValueError as v:
                print("Please enter the valid value.")
        return move

    def makeMove(self,board,move,letter):
        """
        Update the move into the board.
        :param board:
        :param move:
        :param letter:
        :return: Nothing
        """
        if self.isSpaceavailable(board,move):
            board[len(board) - move] = letter;

    def isBoardFull(self):
        """
        Check the self.board is full or not.
        :param self.board:
        :return: Boolean
        """
        for i in range(1,10):
            if i in self.board:
                return False
        return True

    def getMovementFromComputer(self):
        """
        Function will first check the winning position if any available. If any winning position available then it tries to win it.
        Second it will check the position where the player can win and block that position.
        Rest is just an idea to make the game tie.
        Still winning of the game depends upon the user inputs.
        :return:
        """

        for i in [1,2,3,4,5,6,7,8,9]:
            temp = copy.deepcopy(self.board)
            if self.isSpaceavailable(temp,i):
                self.makeMove(temp,i,self.computerLetter)
                if self.isWinner(temp,self.computerLetter):
                    return i

        for i in [1,2,3,4,5,6,7,8,9]:
            temp = copy.deepcopy(self.board)
            if self.isSpaceavailable(temp,i):
                self.makeMove(temp,i,self.playerLetter)
                if self.isWinner(temp,self.playerLetter):
                    return i

        if self.isSpaceavailable(self.board, 5):
            return 5

        otherMove = [i for i in [1,2,3,4,5,6,7,8,9] if self.isSpaceavailable(self.board, i)]
        if len(otherMove) > 0:
            return choose.choice(otherMove)

    def letsplay(self):
        """
        The logic of the game is written here.
        :return: Nothing
        """
        inPlay = True
        while inPlay:
            if self.turn == 'player':
                self.printBoard()
                move = self.getMovementFromPlayer()
                self.makeMove(self.board,move,self.playerLetter)
                if self.isWinner(self.board,self.playerLetter):
                    self.printBoard()
                    print("You Won...!!!")
                    inPlay = False
                else:
                    if self.isBoardFull():
                        self.printBoard()
                        print("It's a Tie...!!!")
                        inPlay = False
                    else:
                        self.toggleTurn()
            else:
                move = self.getMovementFromComputer()
                self.makeMove(self.board, move, self.computerLetter)
                if self.isWinner(self.board, self.computerLetter):
                    self.printBoard()
                    print("Computer Won...!!!")
                    inPlay = False
                else:
                    if self.isBoardFull():
                        self.printBoard()
                        print("It's a Tie...!!!")
                        inPlay = False
                    else:
                        self.toggleTurn()

if __name__ == '__main__':
    while True:
        t = TictocToe()
        if input('Do you want to play again? (yes or no)').lower().startswith('y') != 'y':
            break
