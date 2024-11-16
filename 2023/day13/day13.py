with open('input.txt') as f:
  s = f.read().strip()

patterns =  s.split('\n\n')

def find_mirror(grid):
  for r in range(1, len(grid)):
    above = grid[:r][::-1]
    below = grid[r:]

    # above = above[:len(below)]
    # below = below[:len(above)]

    if sum(sum(0 if a == b else 1 for a, b in zip(x,y)) for x,y in zip(above, below)) == 1:
      return r
  return 0

total = 0

for block in patterns:
  grid = block.splitlines()
  row = find_mirror(grid)
  total += row*100

  col = find_mirror(list(zip(*grid)))
  total += col
  
print(total)