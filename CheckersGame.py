# Author: Duong Tran
# GitHub username: dami1025
# Date: 3/19/2023
# Description: This portfolio project will create a class called Checkers that allows two people to play the game of Checkers. This is a variation of the original Checkers game with modified rules.
#If a piece crosses the board, becomes a king, and then crosses the board back to its original side, it becomes a triple king and gains two abilities in addition to the King’s abilities.
#It can jump: friendly pieces to travel faster. Pieces of the same color are friendly pieces, or two enemy pieces that are right next to each other in one jump; the two enemy pieces will be captured. Two enemy pieces need not be next to the King.

class OutofTurn(Exception):

    """Raise when a player attempts to play the game when it's not their turn"""
    pass

class InvalidSquare(Exception):

    """Raise if the player doesn't own the checker in the selected square location; or when the designated square does not
    exist on the board"""
    pass

class InvalidPlayer(Exception):

    """Raise if the players name is not valid"""
    pass

class InvalidMove(Exception):

    """Raise if the players make an invalid move"""
    pass


class Checker_Piece:

    """Represent a checker object to be used in the Checkers game class. This checker object has parameters of color, row and column and
     methods to return its color, its direction, and to promote a piece in to a King or a Triple King"""
    def __init__(self, color, row, column):

        """Creates a  checker object with the color, king and triple king status, and its direction set by the color of the piece"""

        self._color = color
        self._is_king = False #The piece is initially a normal piece, so both is_king and is_triple_king are set to False
        self._is_triple_king = False
        if self._color == "Black":
            self._direction = -1 #Black piece are placed at the bottom of board, so to move up, the row will go -1 row up
        else:
            self._direction = 1 #White piece are placed at the top of board, so to move up, the row will go 1 row up


    def get_color(self):

        """Return the color of the checker piece item"""

        return self._color

    def get_direction(self):

        """Return the color of the checker piece item"""

        return self._direction

    def make_king(self):

        """If the piece movement during the game satisfy the condition to become a King, make the piece a King"""

        self._is_king = True
    def make_triple_king(self):

        """If the piece movement during the game satisfy the condition to become a Triple King, make the piece a Triple King"""

        self._is_triple_king = True


class Checkers:

    """Represent the Checkers game object as played. It contains information about the board and the players. The board is initialized when the Checkers object is created.
    It also contains various methods to interact with the chessboard."""
    def __init__(self):

        """Creates a  checkers object with no parameterm but it will initialize the board, the players, who is the current player, and the players' turn"""

        self._board = [] #Create an empty list to hold the board later on when the game start
        self._players = {"White": None, "Black": None} #Only 2 classes of player, Black and White
        self._two_players = [] #Creating an empty list to hold turn of current player based on their pieces' color
        self._current_player = None #Current player is intially None
        self._turn = "Black" #Black piece always go first
        self.setup_board() #Call the board set up to start game


    def check_if_valid_square(self, square_location):

        '''Checks to make sure that the square location is valid'''

        row, column = square_location
        if row > 7 or column > 7 or row < 0 or column < 0: #Since this is a 8x8 board, if rows and columns are > 7 or < 0, they are invalid positions
            return False
        else:
            return True

    def setup_board(self):

        """Clears and fills the board data member with a freshly set board for a new game of Checkers
        Set the current player to one that pick Black checker pieces"""

        self._board.clear()

        for rows in range(8):
            row = []
            for columns in range(8):
                if (rows + columns) % 2 != 0 and rows < 3: #White piece at the top, and will be placed at odd position
                    row.append(Checker_Piece("White", rows, columns))
                elif (rows + columns) % 2 != 0 and rows > 4: #Black piece at the bottom, and will be placed at even position
                    row.append(Checker_Piece("Black", rows, columns))
                else:
                    row.append(None)
            self._board.append(row)

        self._two_players.append(Player("First", "Black"))
        self._two_players.append(Player("Second", "White"))
        self._current_player = self._two_players[0] #For this game, the first player is always Black checker, and there's only two options for color, so first current player will be set to Black

    def create_player(self, player_name, piece_color):

        """Creates Player object by name and piece color and adds it to the players dictionary"""

        if player_name in self._players.values(): #Assuming two different players are playing together
            raise InvalidPlayer("Player name already exists")

        player = Player(player_name, piece_color) #Call the Player class to create a player, then add to the dictionary
        self._players[piece_color] = player
        return player

    def get_players(self):

        """Return the dictionary of players in the game"""

        return self._players
    def get_turn(self):

        """Return the turn of players (by piece's color) in the game"""

        return self._turn

    def lookup_player_from_name(self, name):

        """Returns the Player object corresponding to the name, or
        None if no such Player is a member"""

        for person_id in self._players.values():  # Looping through the self._players dictionary to find the matching player name
            #print(person_id)
            if person_id.get_name() == name:
                return person_id #Return that player
            continue
        return None

    def lookup_color_from_player(self, name):

        """Returns the Player object's piece's color corresponding to the name, or
        None if no such Player is a member"""

        for player in self._players.values():  #Looping through the self._players dictionary to find the matching player name
            if player.get_name() == name:
                return player.get_color() #If found, return that player's piece's color
            continue
        return None


    def play_game(self, player_name, starting_square_location, destination_square_location):

        """This method, with three parameters: player's name; starting piece location and ending piece location, take a player, check to see if it is that player's turn,
        if it is then make the move of the checker piece at starting square location to the destination square. During this move, if it resulted in a piece captured, increase the
        player's captured piece count"""

        player = self.lookup_player_from_name(player_name) #Creating a player object based on their name

        #Checking for exceptions/errors associated with the players and the square's location on board
        if player == None:
            raise InvalidPlayer("Player name already exists")
        if self._turn != self.lookup_color_from_player(player_name): #current turn is not current player's color
            raise OutofTurn("It's not your turn to play")
        if self.check_if_valid_square(starting_square_location) is False: #checking if starting square is in range of board
            raise InvalidSquare
        if self.check_if_valid_square(destination_square_location) is False: #checking if destination square is in range of board
            raise InvalidSquare

        row1, column1 = starting_square_location

        row2, column2 = destination_square_location

        checker = self._board[row1][column1] #Create a checker piece object on the starting_square_location tuple

        #Checking for exceptions/errors associated with the checker pieces' current and move to location
        if checker is None:
            raise InvalidMove("No checker in start position")
        if self._board[row2][column2] is not None:
            raise InvalidMove("End position not empty")

        if abs(row2 - row1) == 1 and abs(column2 - column1) == 1: #When the checker piece move one diagonal space forward (toward the opponent’s checkers) during a regular turn.
            self._board[row1][column1] = None #If the move is valid, remove the checker at old position
            self._board[row2][column2] = checker #Move it to new location
        elif abs(row2 - row1) == 2 and abs(column2 - column1) == 2: #If a checker wants to jump an opponent piece, when it moves more than 1 square, check if the space in the middle is occupied and then capture the piece if it is.
            x_cap, y_cap = (row1 + row2) // 2, (column1 + column2) // 2 #The location of the middle piece if a jump happens
            captured_checker = self._board[x_cap][y_cap]
            if captured_checker is None or captured_checker.get_color() == self._current_player.get_color(): #If there's nothing in the middle or if the piece in the middle is on our side
                raise InvalidMove("Invalid capture")
            self._board[row1][column1] = None
            self._board[row2][column2] = checker #Move checker to new pos
            self._board[x_cap][y_cap] = None #Take the captured piece off the board
            player.set_captured_pieces() #Increment the player's captured piece count
            #print("Capture!")
        else:
            raise InvalidMove("Invalid move") #Else, invalid move

        #Make kings and triple kings
        if (checker.get_direction() == 1 and row2 == 7) or (checker.get_direction() == -1 and row2 == 0): #If white piece move to row 7 (the row of Black), it will be a White king.
            checker.make_king()                                                                           #If black piece move to row 0 (the row of White), it will be a Black king.
            player.set_king_count() #Increase the king count
            if (checker.get_direction() == 1 and row2 == 0) or (checker.get_direction() == -1 and row2 == 7): #If after the moves above, they cross back over to their old side, they will become Triple king
                checker.make_triple_king()
                player.set_triple_king_count() #Increase the triple king count

        self._turn = "White" if self._turn == "Black" else "Black" #Change turn of player
        self._current_player = self._two_players[(self._two_players.index(self._current_player) + 1) % 2] #Change current player turn to match board turn in game

        return player.get_captured_pieces_count() #return the number of piece captured


    def get_checkers_details(self, square_location):

        """Checks if the piece's location is in the valid range of the board, then loops through the board to return the detail status of the checker piece"""

        x, y = square_location

        if not self.check_if_valid_square(square_location): #Check if square location is valid
            raise InvalidSquare("Invalid square location")

        checker = self._board[x][y] #Check if checker is present in the square
        if checker is None:
            return None

        #Return the checker details: their color and if they are a king or triple king
        if checker.get_color() == "Black":
            if checker._is_king:
                if checker._is_triple_king:
                    return "Black_Triple_King"
                else:
                    return "Black_king"
            else:
                return "Black"
        else:
            if checker._is_king:
                if checker._is_triple_king:
                    return "White_Triple_King"
                else:
                    return "White_king"
            else:
                return "White"

    def print_board(self):

        """Prints the current board in the form of an array."""

        for rows in range(8):
            row = []
            for columns in range(8):
                piece = self._board[rows][columns]
                if piece is None:
                    row.append(None)
                else:
                    row.append(piece.get_color() + ('_King' if piece._is_king else '') + (
                        '_Triple_King' if piece._is_triple_king else '')) #Print the name of the piece
            print(row)


    def game_winner(self):

        """Return the winner of the game. The winner will have to capture all the enemy pieces,
        or display "Game has not ended" if the game isn't over yet"""

        white_pieces = [] #Create two empty lists to hold the present piece on the board by color
        black_pieces = []

        for row in self._board: #Iterate over the board and add the pieces to their respective lists
            for piece in row:
                if piece is not None and piece.get_color() == "White":
                    #if piece._is_king() or piece._is_triple_king():
                    white_pieces.append(piece)
                elif piece is not None and piece.get_color() == "Black":
                    #if piece._is_king() or piece._is_triple_king():
                    black_pieces.append(piece)

        if len(white_pieces) == 0: #Check if either player has no pieces left (length of list will be 0)
            return "Black"
        elif len(black_pieces) == 0:
            return "White"

        return "Game has not ended"  #If both players have pieces left, the game has not ended


class Player:

    """Player class which contains name, color, set king and triple king status to False initially, and details about number of pieces captured."""

    def __init__(self, player_name, color):
        self._player_name = player_name
        self._color = color
        self._captured_pieces = 0
        self._king_pieces = 0
        self._triple_king_pieces = 0

    def get_name(self):

        """Returns the player's name"""

        return self._player_name

    def get_color(self):

        """Returns the player's color pick"""

        return self._color

    def get_king_count(self):

        """Returns the number of kings the player has"""

        return self._king_pieces

    def set_king_count(self):

        """Increments the number of king_pieces by 1 every time the method is called"""

        self._king_pieces += 1

    def get_triple_king_count(self):

        """Returns the number of triple kings the player has"""

        return self._triple_king_pieces

    def set_triple_king_count(self):

        """Increments the number of triple kings by 1 every time the method is called"""

        self._triple_king_pieces += 1

    def get_captured_pieces_count(self):

        """Returns the amount of pieces the player has captured"""

        return self._captured_pieces

    def set_captured_pieces(self):

        """Increment captured pieces by 1 every time the method is called"""

        self._captured_pieces += 1



