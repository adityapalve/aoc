with open('input.txt') as f:
    grid =  f.read().strip().split('\n')


# grid = [[char for char in line] for line in grid]
# rows = len(grid)
# cols = len(grid[0])
# count = 0

# def dfs(grid, r, c):
#     if (c<0 or r<0 or c>cols or r>rows):
#         return
    
#     if(grid[r][c] == '#'):
#         dfs(grid, r)
#     grid[r][c] = 'X'
#     dfs(grid, r+1,c)
#     dfs(grid, r-1,c)
#     dfs(grid, r,c+1)
#     dfs(grid, r,c-1)

# for r in len(rows):
#     for c in len(cols):
#         if grid[r][c] == '^':
#             dfs(grid,r,c)

R = len(grid)
C = len(grid[0])

for r in range(R):
    for c in range(C):
        if grid[r][c] == '^':
            sr, sc = r, c
p1, p2 = 0,0
for o_r in range(R):
    for o_c in range(C):
        r, c = sr, sc
        d = 0
        seen = set()
        seen_rc = set()
        while True:
            if(r,c,d) in seen:
                p2+=1
                break
            seen.add((r,c,d))
            seen_rc.add((r,c))
            dr, dc = [(-1,0),(0,1),(1,0),(0,-1)][d]
            rr = r+dr
            cc = c+dc
            if not(0<=rr<R and 0<=cc<C):
                if grid[o_r][o_c] == '#':
                    p1 = len(seen_rc)
                break
            if grid[rr][cc] == '#' or rr==o_r and cc==o_c:
                d = (d+1)%4
            else:
                r = rr
                c = cc
print(p1)
print(p2)

def count_obs_positions(grid):
    dir = ['^', '>', '<','v']
    mov = {'^': (-1,0), '>':(0,1), 'v':(1,0), '<':(0,-1)}

    rows, cols = len(grid), len(grid[0])
    guard_pos = None
    guard_dir = None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in dir: 
                guard_pos = (r,c)
                guard_dir = grid[r][c]
                break
        if guard_pos:
            break

    valid_pos = [
        (r,c) for r in range(rows) for c in range(cols)
        if grid[r][c] == '.' and (r,c) != guard_pos
    ]

    def simulate_with_obs(grid, obs):
        mut_map = [list(row) for row in grid]
        mut_map[obs[0]][obs[1]] = '#'

        visited_sates = set()
        curr_pos = guard_pos
        curr_dir = guard_dir

        while True:
            state = (curr_pos, curr_dir)
            if state in visited_sates:
                return True
            visited_sates.add(state)
            dr, dc = mov[curr_dir]
            if (curr_pos[0] < rows and 0 <= next_pos[1] < cols):
                return False
            


valid_obs_count = 0
for obs in valid_pos:
    if simulate_with_obs(grid, obs):
        valid_obs_count += 1