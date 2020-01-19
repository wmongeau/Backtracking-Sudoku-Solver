# Sudoku Solver

This program is a sudoku solver written in **Python**. It uses a **backtracking** algorithm that essentially tries values for each square in the suoku puzzle by traversing the puzzle. Once it finds a valid value for a given square, it moves on to the next square. If it gets to a sqaure where it can't find a valid value, it will go back to the previous ssqaure and see if it can find a different valid value and continue solving the puzzler as before. If it can't find a valid value at the previous sqaure, it will once more go back one square and try and find a valid value.

### Planned additions
 I would like to add a UI to this application that allows the user to observe the solving of the puzzle. Also, I would like to add image recognition to facilitate the input of a new sudoku puzzle.
