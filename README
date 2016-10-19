A quick and dirty 'proof' by exhaustion for Math 248 (Methods of Proofs), with
Dr. Todd Grundmeier, Fall 2016.

Proposition 2.43: "There does not exist a truce of six queens on a 6x6 chess
board in which a corner of the board is occupied."

Uses a brute force with backtracking algorithm. Essentially:
1. Start with a queen in the corner and at the 0,1 square.
2. Place a queen in the current spot.
3. If the board is invalid, remove the queen.
4. If we're at the last square and the board was invalid or there are fewer
than six queens on the board, backtrack to the previous queen and remove it.
(We'll loop back around and try the next valid spot for that previous queen;
the backtracking persists for step 7.)
5. If we have to backtrack all the way to the first square, there is no
solution.
6. If, at any time, the board is valid and there are six queens on the board,
we have found the solution.
7. Move to the next spot.
