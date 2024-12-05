with open('test.txt') as f:
    grid = f.read().splitlines()

def dfs(grid, word, x, y, dx, dy):
    for i in range(len(word)):
        nx, ny = x + i * dx, y + i * dy
        if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] != word[i]:
            return False
    return True

def search_word(grid, word):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    found_positions = []
    
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == word[0]:
                for dx, dy in directions:
                    if dfs(grid, word, x, y, dx, dy):
                        found_positions.append((x, y, dx, dy))
    
    return found_positions


# Convert grid to list of lists
grid = [list(row) for row in grid]
# print(grid)
# Search for the word 'XMAS'
word = "XMAS"
positions = search_word(grid, word)
print(len(positions))