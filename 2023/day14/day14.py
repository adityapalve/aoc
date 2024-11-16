with open("input.txt") as f:
  s = f.read().strip()
grid = s.splitlines()
for i,r in enumerate(grid):
  grid[i] = [x for x in r]

rows = len(grid)
cols = len(grid[0])

for c in range(cols):
  for _ in range(rows):
    for r in range(rows):
      if r>0 and grid[r][c] == "O" and grid[r-1][c] == ".":
        grid[r-1][c] = "O"
        grid[r][c] = "."

ans = 0
for r in range(rows):
  for c in range(cols):
    if grid[r][c] == "O":
      ans += rows-r

print(ans)