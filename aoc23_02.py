# Advent of Code 2023
# Day 2


def is_legit(pull):
    # test whether all of a set of cube pulls fall within parameters for a legal set
    color_max = {"red": 12, "green": 13, "blue": 14}
    cubes = pull.split(', ')
    for c in cubes:
        val, space, color = c.partition(' ')
        if color_max[color] < int(val):
            return False
    return True


def problem_one():
    file = open("input_02.txt")
    total = 0

    for line in file:
        legit = True
        line = line.removesuffix('\n')
        line = line.removeprefix('Game ')
        game_id, colon, pull_list = line.partition(': ')
        pulls = pull_list.split('; ')
        for p in pulls:
            if not is_legit(p):
                legit = False
                break
        if legit:
            total += int(game_id)

    print(f'Problem one total: {total}')


def problem_two():
    file = open("input_02.txt")
    total = 0

    for line in file:
        legit = True
        line = line.removesuffix('\n')
        line = line.removeprefix('Game ')
        game_id, colon, pull_list = line.partition(': ')
        pulls = pull_list.split('; ')
        maxes = {"red": 0, "green": 0, "blue": 0}

        for p in pulls:
            cubes = p.split(', ')
            for c in cubes:
                val, space, color = c.partition(' ')
                if maxes[color] < int(val):
                    maxes[color] = int(val)
        power = maxes["red"] * maxes["green"] * maxes["blue"]
        total += power

    print(f'Problem two total: {total}')

problem_one()
problem_two()
