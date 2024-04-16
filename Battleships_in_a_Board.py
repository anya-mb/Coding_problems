"""
## 419. Battleships in a Board
Medium

Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

 

### Example 1:


Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2

### Example 2:

Input: board = [["."]]
Output: 0
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is either '.' or 'X'.
 

Follow up: Could you do it in one-pass, using only O(1) extra memory and without modifying the values board?

## Solution

The problem description specifies that each battleship occupies a straight line either horizontally (1 x k) or vertically (k x 1) and no two battleships touch one another. To identify each battleship distinctly, we can designate a specific cell within each battleship as its representative cell, which we'll refer to as the 'leader'. By counting these leader cells, we can determine the total number of battleships.

For identifying a leader within each battleship, we will consider the topmost (and if there are ties, then the leftmost) cell of the battleship cells as its leader.

To efficiently identify whether a cell acts as a leader, we leverage the fact that a leader is always positioned in the top-left cell of a battleship, and no two battleships are adjacent. Therefore, a cell marked 'X' qualifies as a leader if neither the cell directly to its left (board[i][j-1]) nor the cell directly above it (board[i-1][j]) contains an 'X'. Conversely, any non-leader 'X' cell will always be adjacent to another 'X' either to the left or above, ensuring it is not mistakenly counted as a leader. To determine the total number of leaders, we simply traverse all cells and count those that meet this leader criterion.

### Time Complexity
Each cell check to determine if it is a leader is constant, O(1), and since the grid size is MxN, checking all cells results in a time complexity of O(MN).

### Space Complexity
The algorithm uses a simple counter to track the number of leaders, thus requiring only constant space, O(1).

"""

WATER_CONST = '.'
SHIP_CONST = 'X'

def count_battleships(board: List[List[str]]) -> int:
    n = len(board)
    m = len(board[0])
    
    result = 0
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == SHIP_CONST:
                if (i == 0 or board[i - 1][j] == WATER_CONST) and \
                   (j == 0 or board[i][j - 1] == WATER_CONST):
                    result += 1
    
    return result

def test():
    board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]

    result = count_battleships(board)
    expected_result = 2

    assert result == expected_result


    board = [["."]]

    result = count_battleships(board)
    expected_result = 0

    assert result == expected_result

test()