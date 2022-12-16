from PIL import Image, ImageDraw

frames = []


def draw_grid(grid, min_x, max_x, max_y):
    image = Image.new("RGB", (max_x + 4 - min_x, max_y + 3), "white")
    draw = ImageDraw.Draw(image)
    height = len(grid)
    width = len(grid[0])
    for y in range(height)[:max_y + 2]:
        for x in range(width)[min_x - 2:max_x + 2]:
            char = grid[y][x]
            x_offset = x - min_x
            if char == 1:
                draw.point([x_offset, y], 'red')
            elif char == 2:
                draw.point([x_offset, y], 'yellow')

    frames.append(image)


def read_data(test, file):
    if test:
        path = file
    else:
        path = './input.txt'
    file = open(path, 'r')
    lines = file.readlines()
    for i, line in enumerate(lines):
        lines[i] = line.replace('\n', '')
    return lines


def main(test=False):
    lines = read_data(test, "./test_input.txt")
    frames = []

    grid = [[0] * 1000 for i in range(1000)]

    x_max, y_max = 0, 0
    x_min = 1000

    for line in lines:
        grid, rock_x_min, rock_x_max, rock_y_max = add_rock(grid, line)
        y_max = max([rock_y_max, y_max])
        x_max = max([rock_x_max, x_max])
        x_min = min([rock_x_min, x_min])

    draw_grid(grid, x_min, x_max, y_max)
    result, grid = sand_loop(grid, x_min, x_max, y_max)

    frames[0].save("sand.gif", format="GIF", append_images=frames,
                   save_all=True, duration=120, loop=0)

    return result


def main_2(test=False):
    lines = read_data(test, "./test_input.txt")
    frames = []
    
    grid = [[0] * 1000 for i in range(1000)]

    x_max, y_max = 0, 0
    x_min = 1000

    for line in lines:
        grid, rock_x_min, rock_x_max, rock_y_max = add_rock(grid, line)
        y_max = max([rock_y_max, y_max])
        x_max = max([rock_x_max, x_max])
        x_min = min([rock_x_min, x_min])

    line = '{},{} -> {},{}'.format(500 - y_max-10, y_max + 2, 500 + y_max + 10, y_max + 2)
    add_rock(grid, line)

    result, grid = sand_loop(grid, x_min, x_max, y_max, 2)

    frames[0].save("sand_2.gif", format="GIF", append_images=frames,
                   save_all=True, duration=120, loop=0)

    return result


def sand_loop(grid, x_min, x_max, y_max, offset=1):
    sand_start = [500, 0]

    for x in range(50000):
        if grid[sand_start[1]][sand_start[0]] == 2:
            return x, grid

        _, grid, end = drop_sand(grid, sand_start, y_max + offset)
        if x % 1000 == 0:
            print_grid(grid, x_min-100, x_max+100, y_max+5)
        if x % 100 == 0:
            draw_grid(grid, x_min-100, x_max+100, y_max+5)
        if end:
            return x, grid


def drop_sand(grid, sand_pos, max_y):
    sand_x, sand_y = sand_pos

    if sand_y == max_y:
        return False, grid, True

    can_fall = False

    check_bottom_left = sand_x - 1
    check_bottom_right = sand_x + 1
    check_bottom = sand_y + 1

    # check below
    if grid[check_bottom][sand_x] == 0:
        sand_pos = [sand_x, check_bottom]
        can_fall = True
    # check bottom left
    elif grid[check_bottom][check_bottom_left] == 0:
        sand_pos = [check_bottom_left, check_bottom]
        can_fall = True
        # check bottom left
    elif grid[check_bottom][check_bottom_right] == 0:
        sand_pos = [check_bottom_right, check_bottom]
        can_fall = True

    if can_fall:
        return drop_sand(grid, sand_pos, max_y)
    else:
        grid[sand_pos[1]][sand_pos[0]] = 2
        return False, grid, False


def add_rock(grid, line):
    points = line.split(' -> ')

    max_y, max_x = 0, 0
    min_x = 1000
    for i, p in enumerate(points):
        points[i] = p.split(',')
        points[i][0] = int(points[i][0])
        points[i][1] = int(points[i][1])

    prev_point = points[0]

    for next_point in points[1:]:
        prev_x, prev_y = prev_point
        next_x, next_y = next_point
        x_dif = next_x - prev_x
        y_dif = next_y - prev_y

        if x_dif != 0:
            direction = x_dif // abs(x_dif)
            for i in range(prev_x, next_x, direction):
                grid[prev_y][i] = 1

        elif y_dif != 0:
            direction = y_dif // abs(y_dif)
            for i in range(prev_y, next_y, direction):
                grid[i][prev_x] = 1

        grid[next_y][next_x] = 1
        prev_point = next_point

    for p in points:
        max_y = max([max_y, p[1]])
        max_x = max([max_x, p[0]])
        min_x = min([min_x, p[0]])

    return grid, min_x, max_x, max_y


def print_grid(grid, x_min, x_max, y_max):
    string = ''
    height = len(grid)
    width = len(grid[0])
    for y in range(height)[:y_max + 3]:
        string += '\n'
        for x in range(width)[x_min:x_max]:
            char = grid[y][x]
            if char == 1:
                string += '#'
            elif char == 2:
                string += 'o'
            else:
                string += '.'

    print(string)


print("Test 1", (main(True) == 24))
print("Answer 1", main())

print("Test 1", (main_2(True) == 93))
print("Answer 1", main_2())
