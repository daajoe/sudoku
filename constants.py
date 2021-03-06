from enum import Enum

SUDOKU_GRID_SIZE = 9
ERROR_VALUE = -1
EMPTY_CELL_VALUE = -2
SUDOKU_VALUE_RANGE = (1, 9)

class Cell(Enum):
    ERROR = -1
    EMPTY = -2
