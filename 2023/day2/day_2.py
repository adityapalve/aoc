file_1 = open("input.txt", "r")
test_input = open("test.txt", "r")

def parse(line, all_ids, invalid_games):
  cubes = {
    "red"   :0,
    "green" :0, 
    "blue"  :0 
  }
  game_id, distribution = line.split(':')
  game_id = game_id.split()[-1]
  all_ids.append(int(game_id))
  # print(game_id)
  # print(game_id," Cubes:", distribution)
  games = distribution.split(';')
  for game in games:
    cubes_revealed = game.split(',')
    for c in cubes_revealed:
      num, colour = c.split()
      if int(num) > cubes[colour]:
        invalid_games.append(int(game_id))


def part1(file):
  lines = file.readlines()
  all_ids = []
  invalid_games = []
  for line in lines:
    parse(line, all_ids, invalid_games)

  res = set(all_ids) - set(invalid_games)
  print(res, sum(res))


# part1(file_1)


"""
Part 2: Day-2
"""
def parse_2(line, res):
  cubes = {
    "red"   :0,
    "green" :0, 
    "blue"  :0 
  }
  game_id, distribution = line.split(':')
  game_id = game_id.split()[-1]
  # all_ids.append(int(game_id))
  # print(game_id)
  # print(game_id," Cubes:", distribution)
  games = distribution.split(';')
  for game in games:
    cubes_revealed = game.split(',')
    for c in cubes_revealed:
      num, colour = c.split()
      cubes[colour] = max(int(num), cubes[colour])
  
  values = list(cubes.values()) 
  power = 1
  for i in values:
    power *= i

  res.append(power)

file2 = open("input2.txt", 'r')

def part2(file):
  lines = file.readlines()
  res = []
  for line in lines:
    parse_2(line, res)

  print(sum(res))

part2(file2)