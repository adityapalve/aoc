file_1 = open("input.txt", "r")
file_2 = open("input_f.txt", "r")
file_3 = open("input2.txt", "r")

def foo_part_1(file):
    nums = []
    for line in file.readlines():
        digits = [int(i) for i in line if i.isdigit() == True]
        if len(digits) <= 1:
            fd, ld = digits[0], digits[0]
        else:
            fd, ld = digits[0], digits[-1]
        num = str(fd) + str(ld)
        # print(fd, ld, num)
        nums.append(int(num))
    return sum(nums)


def find_number(line):
    numbers = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    string = ""
    nums = []
    for i in line:
        if i.isdigit():
            nums.append(int(i))
            string = ""
        else:
            string += i
            if any(number.startswith(string) for number in numbers):
                if string in numbers.keys():
                    nums.append(numbers[string])
                    string = ""
            else:
                print(string)
                string = ""
    return print(nums)


def find_number_bt(line):
    numbers = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    nums = []
    i = 0
    while i < len(line):
        string = ""
        found = False
        for j in range(i, len(line)):
            if line[j].isdigit():
                if string:
                    if string in numbers:
                        nums.append(numbers[string])
                        i = j  # Move i to the current digit
                        found = True
                        break
                    else:
                        break  # Break if string is not a valid number word
                nums.append(int(line[j]))
                i = j + 1
                found = True
                break
            else:
                string += line[j]
                if string in numbers:
                    nums.append(numbers[string])
                    i = j + 1
                    found = True
                    break
        if not found:
            i += 1  # Move to the next character if no number is found

    return nums


def part_2(file):
    lines = file.readlines()
    res = []
    i = 1
    for line in lines:
        l = "".join(line.split())
        nums = find_number_bt(l)
        if len(nums)<= 1:
            fd, ld = nums[0], nums[0]
        else:
            fd, ld = nums[0], nums[-1]
        n = int(str(fd)+str(ld))
        print(i, line, nums, n)
        res.append(int(str(fd)+str(ld)))
        i += 1
    # print(len(res))
    return sum(res)
# print(part_2(file_1))
print(part_2(file_3))