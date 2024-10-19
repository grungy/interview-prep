grid = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0]]

  
  

def getUniquePaths(grid):

    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    path_count = 0

  

    def backtrack(row, col):
        nonlocal grid
        nonlocal path_count
        nonlocal visited

        # bound checking to make sure we stay in the grid
        # if row < 0 or row >= rows or col < 0 or col >= cols:
        #     return

        # if grid[row][col] == 1: # we found a wall and need to backtrack
        #     return

        # if (row, col) in visited:
        #     return

        if row == rows - 1 and col == cols - 1 and grid[row][col] == 0:
            path_count += 1
            return

        
        directions = [(1,0), (0,1)] # down, up, right, left
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and grid[nr][nc] != 1:
                visited.add((nr,nc))
                backtrack(nr,nc)
                visited.remove((nr,nc)) # backtrack by removing from the visited set.

  

    backtrack(0, 0)

    return path_count

  

answer = getUniquePaths(grid)

print(answer)