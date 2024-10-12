# Checkers-Game

CS 162 Portfolio Project

Game Rules

Checkers, also known as draughts, is a fun and easy game that dates back to the 12th century. To win a game of checkers, your goal is to capture or block your opponent's pieces so that they can no longer make a move. You can move faster by jumping your opponent's pieces and removing them from the board.
Board Setup:
The board is made up of 64 alternating dark and light squares which appear in 8 rows of 8. There are 32 light squares and 32 dark squares. Each player will place his/her pieces on the 12 dark squares in the first three rows closest to him or her, as shown in the below figure. The board is arranged such that white square is at top left corner and white pieces are placed at this side of the board (as shown in the figure below)
The checkers may only move in diagonal directions on the dark squares.
Since the board has 8 rows, 6 of the rows will be taken up by the players' checkers and two rows will be left open in the middle of the board.

 


Game Rules (Watch the demonstration of the rules 1 and 2 on ‘https://www.wikihow.com/Play-Checkers’:
1.	The player with black checkers starts the game. You can only move one checker one diagonal space forward (toward your opponent’s checkers) during a regular turn. Checkers must stay on the dark squares. Once the player with black checkers makes their first move, the player with white checkers moves, and then you’ll take turns.
2.	Jump your opponent's checkers to remove them from the board. If your checker is in the diagonal space nearest to one of your opponent's checkers, then you can jump and capture that checker. To capture a checker, move two diagonal spaces in the direction of the checker you’re attacking, like you are hopping over your opponent's piece.
●	The space on the other side of your opponent’s checker has to be empty so that you can move into it.
●	If you have the opportunity to jump your opponent's checker, then the rules state you must jump it.
●	If you have the opportunity to jump your opponent's checker in multiple parts of the board, then you must take that move which will allow you to capture as many pieces as possible.
●	If the new position you land in gives you a direct opportunity to capture another checker, then you must keep going until you can't capture any more of your opponent's checkers.
3.	When one of your pieces reaches the end of your opponent's side it becomes a King.
●	When a piece becomes a King, it continues to move as a King.
●	Kings can still only move one diagonal space at a time during a non-capture move. 
●	Kings can make jumps to any square along a diagonal which contains only one opposing piece which is captured, so the opposing piece does not need to be adjacent to the king, and the ending square of the move does not need to be adjacent to the piece captured.
●	Kings can move both forward and backward.

4.	Triple King: If a piece crosses the board, becomes a king, and then crosses the board back to its original side, it becomes a triple king and gains two abilities in addition to the King’s abilities. 
It can jump:
●	 friendly pieces to travel faster. Pieces of the same color are friendly pieces. 
●	two enemy pieces that are right next to each other in one jump; the two enemy pieces will be captured. Two enemy pieces need not be next to the King.
 

5.	Keep jumping and capturing to win the game. Continue jumping and capturing your opponent's checkers until they are all removed from the board. Once you have captured all your opponent’s checkers, you have won the game!
A checker can jump over an opponent's king or triple king and capture them just as it can capture any opponent piece.
●	A less common way to win is when all of your opponent's pieces are blocked so that your opponent can't make any more moves.

For the purpose of referring to the squares on the board we will use tuple (row_number, column_number). The numbering of rows and columns start from 0. The location of 7th square in 2nd row will have a location of (1,6)
 

Major sections of this document have been taken from below resources:
[1]: https://www.wikihow.com/Play-Checkers
![image](https://github.com/user-attachments/assets/49d9ffa5-b909-4aa1-8169-ebd9c6c0b43e)
