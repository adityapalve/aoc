file_1 = open("input.txt", "r")

def parse(line, all_ids, invalid_games):
  cubes = {
    "red"   :12,
    "green" :13, 
    "blue"  :14 
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


part1(file_1)