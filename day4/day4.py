with open("input.txt") as f:
  s = f.read()
with open("test.txt") as t:
  test = t.read()

def part_1(l):
  res = []
  for x in l.strip().split('\n'):
    card_id, all_nums = x.split(':')

    w_nums, nums = all_nums.split('|')
    w_nums = w_nums.strip().split(' ')
    nums = nums.strip().split(' ')

    count = 0 
    for num in nums:
      if num in w_nums and num!='':
        count += 1

    print(card_id, w_nums, nums, count)
    if count>1:
      points = 2**(count-1)
    elif count == 1:
       points = 1
    else: points = 0 
    res.append(points)
  print(res)
  return sum(res)
    
print(part_1(s))

def count_total_scratchcards(scratchcard_info):
    # Parse the scratchcard information
    cards = []
    for line in scratchcard_info.strip().split('\n'):
        card_id, all_nums = line.split(':')
        w_nums, nums = all_nums.split('|')
        w_nums = set(w_num for w_num in w_nums.strip().split(' ') if w_num != '')
        nums = set(num for num in nums.strip().split(' ') if num != '')
        cards.append((w_nums, nums))
    # print(w_nums, nums)
    # print(cards)
    # Initialize a list to keep track of the number of copies of each card
    card_copies = [1] * len(cards)  # Start with 1 copy of each original card

    # Iterate over each card and determine the number of new copies won
    for i, (w_nums, nums) in enumerate(cards):
        matches = len(w_nums.intersection(nums))
        for j in range(i + 1, min(i + 1 + matches, len(cards))):
            card_copies[j] += card_copies[i]

    # Sum up the total number of scratchcards
    total_scratchcards = sum(card_copies)
    return total_scratchcards
  
print(count_total_scratchcards(s))