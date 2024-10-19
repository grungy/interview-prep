# Dynamic Programming Approach

  

grid = [[0, 0, '1', 0, 0], [0, 0, 0, 0, 0], [0, '1', 0, 0, 0]]
rows = len(grid)
cols = len(grid[0])
  

grid[0][0] = 1

  

# Fill the first row
for col in range(1, cols):
    if grid[0][col] != '1':
        grid[0][col] = grid[0][col - 1]  # Only reachable if the previous cell was not a wall
    else:
        grid[0][col] = 0  # Wall, no paths

# Fill the first column
for row in range(1, rows):
    if grid[row][0] != '1':
        grid[row][0] = grid[row - 1][0]  # Only reachable if the cell above was not a wall
    else:
        grid[row][0] = 0  # Wall, no paths

# Process the rest of the grid
for row in range(1, rows):
    for col in range(1, cols):
        if grid[row][col] != '1':
            # Sum the paths from the top and left cells
            grid[row][col] = grid[row - 1][col] + grid[row][col - 1]
        else:
            grid[row][col] = 0  # Wall, no paths

print(grid[rows-1][cols-1])