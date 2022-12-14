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
    
    height_map, start, end = setup_map(lines)
    
    steps = run_search(height_map, start, end)
    
    return steps

def main_2(test=False):
    lines = read_data(test, "./test_input.txt")
    
    height_map, start, end = setup_map(lines)
    
    steps = run_search_start(height_map, end)
    
    return steps

def setup_map(lines):
    height = len(lines)
    height_map = [[] for i in range(height)]
    start = [0,0]
    end = [0,0]
    
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == 'S':
                char = 'a'
                start = [i,j]
            elif char == 'E':
                char = 'z'
                end = [i,j]
                
            height_map[i].append(ord(char)-97)
            
    return height_map, start, end

def run_search(height_map, start, end):
    y_max = len(height_map)
    x_max = len(height_map[0])
    distance_map = [[9999] * x_max for i in range(y_max)]
    
    distance_map[start[0]][start[1]] = 0
    
    searched = [start]
    new_search = [start]
    
    for i in range(10000):
        potential = []
        for new in new_search:
            new_distance = distance_map[new[0]][new[1]]
            
            directions = search_directions(new, x_max - 1, y_max - 1, height_map)
            for direction in directions:
                if direction not in searched and direction not in potential:
                    potential.append(direction)
                    prev_distance = distance_map[direction[0]][direction[1]]
                    
                    if prev_distance > new_distance + 1:
                        distance_map[direction[0]][direction[1]] = new_distance + 1
        
        searched = searched + new_search
        new_search = potential
        
        if end in searched:
            return distance_map[end[0]][end[1]]

def run_search_start(height_map, end):
    y_max = len(height_map)
    x_max = len(height_map[0])
    distance_map = [[9999] * x_max for i in range(y_max)]
    
    distance_map[end[0]][end[1]] = 0
    
    searched = [end]
    new_search = [end]
    
    for i in range(50000):
        potential = []
        for new in new_search:
            new_distance = distance_map[new[0]][new[1]]
            
            directions = search_directions_down(new, x_max - 1, y_max - 1, height_map)
            for direction in directions:
                if direction not in searched and direction not in potential:
                    potential.append(direction)
                    prev_distance = distance_map[direction[0]][direction[1]]
                    
                    if prev_distance > new_distance + 1:
                        distance_map[direction[0]][direction[1]] = new_distance + 1
                        distance_height = height_map[direction[0]][direction[1]]
                        if new_distance + 1 > 110:
                            z = 1
                            
                        if distance_height == 0:
                            return new_distance + 1
        
        searched = searched + new_search
        new_search = potential

    return 0

def search_directions_down(point, x_max, y_max, height_map):
    directions = []
    y = point[0]
    x = point[1]
    point_height = height_map[y][x]
    
    if x > 0:
        p = [y, x-1]
        p_height = height_map[p[0]][p[1]]
        if p_height - point_height >= -1:
            directions.append(p)
            
    if x < x_max:
        p = [y, x+1]
        p_height = height_map[p[0]][p[1]]
        if p_height - point_height >= -1:
            directions.append(p)
    
    if y > 0:
        p = [y-1, x]
        p_height = height_map[p[0]][p[1]]
        if p_height - point_height >= -1:
            directions.append(p)
            
    if y < y_max:
        p = [y+1, x]
        p_height = height_map[p[0]][p[1]]
        if p_height - point_height >= -1:
            directions.append(p)        
    
    return directions

def search_directions(point, x_max, y_max, height_map):
    directions = []
    y = point[0]
    x = point[1]
    point_height = height_map[y][x]
    
    if x > 0:
        p = [y, x-1]
        p_height = height_map[p[0]][p[1]]
        if p_height - point_height <= 1:
            directions.append(p)
            
    if x < x_max:
        p = [y, x+1]
        p_height = height_map[p[0]][p[1]]
        if p_height - point_height <= 1:
            directions.append(p)
    
    if y > 0:
        p = [y-1, x]
        p_height = height_map[p[0]][p[1]]
        if p_height - point_height <= 1:
            directions.append(p)
            
    if y < y_max:
        p = [y+1, x]
        p_height = height_map[p[0]][p[1]]
        if p_height - point_height <= 1:
            directions.append(p)        
    
    return directions

print("Test 1", (main(True) == 31))
print("Answer 1", main())

print("Test 2", (main_2(True) == 29))
print("Answer 2", main_2())
