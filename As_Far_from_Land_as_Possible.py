"""
## 1162. As Far from Land as Possible
Medium

Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

 

Example 1:


Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:


Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1

## Solution

Algorithm Description for "As Far from Land as Possible"

### Overview
The task is to find the maximum Manhattan distance from any water cell to the nearest land cell on an n x n grid, where '1' represents land and '0' represents water.

### Approach
The solution employs a Breadth-First Search (BFS) strategy, a common technique for finding the shortest path in grid-like structures. The BFS starts from all land cells simultaneously, which effectively measures the shortest distance to the nearest land for each water cell.

### Steps
1. Initial Checks:

Verify if the grid contains only land or only water. If so, return -1, indicating that a valid maximum distance cannot be determined.

2. Initialization:

Identify all initial land cells and add them to the BFS queue. This setup allows the algorithm to expand outwards from all pieces of land simultaneously.

3. BFS Expansion:

For each cell in the BFS queue, check its neighboring cells (up, down, left, right).
If a neighbor is a water cell (hasn't been visited), mark it as visited by setting it to land (to prevent re-visitation) and add it to the next layer of the BFS queue.

4. Tracking Distance:

Increment a distance counter each time the BFS completes processing of the current layer and moves to the next layer. This counter represents the distance from the land to the current water cells being processed.

5. Termination:

The BFS continues until no more water cells can be visited, meaning the last set of water cells processed were the farthest from any land cell. The distance counter from the last completed layer is the answer, but since the distance is incremented before processing, subtract one to get the correct maximum distance.

### Time Complexity: O(n^2). Each cell is visited exactly once during the BFS expansion. Since there are n^2 cells and each cell's neighbors are checked (at most 4 neighbors), the operation is bound by the total number of cells.

### Space Complexity: O(n^2) for the worst case where almost all cells are part of the BFS queue at some point. Additionally, the grid itself and a few auxiliary data structures (like sets for current and next cells) also contribute to the space complexity but remain within the same order.

"""

from typing import List, Tuple

LAND_CONSTANT = 1
WATER_CONSTANT = 0
NOT_VALID_MAP_CONSTANT = -1

def find_next_moves(cell: Tuple[int, int], n_grid: int) -> List[Tuple[int, int]]:
    """
    Generate a list of valid moves from the current cell on the grid.
    
    Parameters:
        cell (Tuple[int, int]): The current cell's row and column indices.
        n_grid (int): The dimension of the square grid.
        
    Returns:
        List[Tuple[int, int]]: A list of tuples, each representing the row and column index of a valid move.
    """
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    row_idx, col_idx = cell
    return [(row_idx + dr, col_idx + dc) for dr, dc in directions 
            if 0 <= row_idx + dr < n_grid and 0 <= col_idx + dc < n_grid]

def find_the_farthest_distance_from_land(grid: List[List[int]]) -> int:
    """
    Find the maximum Manhattan distance from any water cell to the nearest land cell in an n x n grid.
    
    Parameters:
        grid (List[List[int]]): A 2D grid where '1' represents land and '0' represents water.
        
    Returns:
        int: The maximum distance to the nearest land cell from any water cell, or -1 if the grid is invalid.
    """
    n = len(grid)
    # Check for edge cases where grid is all land or all water
    if all(grid[r][c] == WATER_CONSTANT for r in range(n) for c in range(n)) \
       or all(grid[r][c] == LAND_CONSTANT for r in range(n) for c in range(n)):
        return NOT_VALID_MAP_CONSTANT

    # Initialize BFS with all land cells
    current_cells = {(r, c) for r in range(n) for c in range(n) if grid[r][c] == LAND_CONSTANT}
    if not current_cells:
        return NOT_VALID_MAP_CONSTANT

    current_dist = 0
    # Perform BFS to find the farthest distance to water
    while current_cells:
        current_dist += 1
        next_cells = set()
        for r, c in current_cells:
            # Explore all valid neighbors of the current cell
            for nr, nc in find_next_moves((r, c), n):
                if grid[nr][nc] == WATER_CONSTANT:
                    grid[nr][nc] = LAND_CONSTANT  # Mark as visited by converting to land
                    next_cells.add((nr, nc))
        current_cells = next_cells

    # The final distance is adjusted by subtracting 1 due to the increment after the last layer
    return current_dist - 1
