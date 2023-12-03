# Advent of Code 2023
# Day 3

# Doing building up a 2D array and then making a dict of part ids with their coords and then checking each of those
# is a lot of overhead; a much leaner implementation would be to just do string searches without bothering to unpack
# all this into a matrix and fiddle with it.  But I am tired and this is where my head is at tonight.  I will make
# myself think about regex etc. after all some other day.

# There's a lot of shagginess in this solution.  Forgive the length of the code, I did not have time to make
# it shorter.

def problem_one():
    file = open("input_03.txt")
    matrix = []
    width = 0
    total = 0

    # let's chuck this whole input file into a 2D array, and pad it with a perimeter of '.' literals so that
    # we can search around potential parts numbers without having to worry about bounds checking
    for line in file:
        if len(matrix) == 0:
            # this is the first line we're reading
            width = len(line)
            matrix.append(['.'] * (width + 2))
        new_row = [x for x in line]
        new_row.insert(0, '.')
        new_row.insert(-1, '.')
        matrix.append(new_row)
    matrix.append(['.'] * (width + 2))

    # now lets just go find all the numeric strings in the matrix
    manifest = {}
    gearbox = {}
    for y in range(1, len(matrix) - 1):
        building = False
        id_str = ''
        x_orig = 0
        for x in range(1, width + 1):
            if matrix[y][x].isdigit():
                if not building:
                    # we have the start of a potential part id; cobble together any following digits to get the full id
                    id_str = matrix[y][x]
                    building = True
                    x_orig = x
                else:
                    id_str += matrix[y][x]
            else:
                if building:
                    building = False
                    manifest[(y, x_orig)] = id_str

            # and a bit of extra bookkeeping for problem two: where are the gears?
            if matrix[y][x] == '*':
                gearbox[(y, x)] = []

    # now for each id we found, check the characters within the 1-padded bounding rectangle for any
    # non-digit, non-. characters that indicate this is a keeper
    for coords in manifest:
        y = coords[0]
        x = coords[1]
        id_str = manifest[coords]
        match = False
        test_char = ''
        for dy in range(y - 1, y + 2):
            for dx in range(x - 1, x + len(id_str) + 1):
                test_char = matrix[dy][dx]
                if not test_char.isdigit() and not test_char == '.':
                    # we've got a symbol, we can quit and call this a match
                    match = True
                    # and a bit for problem two:
                    if test_char == '*':
                        gearbox[(dy, dx)].append(id_str)
            if match is True:
                total += int(id_str)
                print(f'line {y} id_str {id_str} is valid, adjacent to symbol {test_char}')
                break

    total_two = 0
    for coords in gearbox:
        neighbors = gearbox[coords]
        if len(neighbors) == 2:
            gear_ratio = int(neighbors[0]) * int(neighbors[1])
            total_two += gear_ratio

    print(f'Problem one total: {total}')
    print(f'Problem two total: {total_two}')


problem_one()
