def read_data(test):
    if test:
        path = './test_input.txt'
    else:
        path = './input.txt'
    file = open(path, 'r')
    lines = file.readlines()
    for i, line in enumerate(lines):
        lines[i] = line.replace('\n', '')
    return lines

def read_data_2(test):
    if test:
        path = './test_input_2.txt'
    else:
        path = './input.txt'
    file = open(path, 'r')
    lines = file.readlines()
    for i, line in enumerate(lines):
        lines[i] = line.replace('\n', '')
    return lines
    
def main(test=False):
    lines = read_data(test)
    
    visited_dictionary = {'0,0':True}
    
    head = [0,0]
    tail = [0,0]
    
    for line in lines:
        commands = line.split(' ')
        x_move, y_move = get_direction_vector(commands[0])
        for moves in range(int(commands[1])):
            head[0] += x_move
            head[1] += y_move
            
            tail = move_tail(head, tail)
            coords = '{x},{y}'.format(x=tail[0],y=tail[1])
            visited_dictionary[coords] = True

    return len(visited_dictionary.keys())

def get_direction_vector(command):
    if command == 'U':
        return 0,1
    if command == 'R':
        return 1,0
    if command == 'D':
        return 0,-1
    if command == 'L':
        return -1,0
            
def move_tail(head, tail):
    x_dist = head[0] - tail[0]
    y_dist = head[1] - tail[1]
    
    # Dont move if touching
    if abs(x_dist) <=1 and abs(y_dist) <=1:
        return tail
    
    x_move = 0
    y_move = 0
    
    if x_dist >= 1:
        x_move = 1
    elif x_dist <= -1:
        x_move = -1
        
    if y_dist >= 1:
        y_move = 1
    elif y_dist <= -1:
        y_move = -1
        
    tail[0] += x_move
    tail[1] += y_move
    
    return tail
            
def main_2(test=False):
    lines = read_data_2(test)
    
    visited_dictionary = {'0,0':True}
    positions = [[0,0] for i in range(10)]
    
    for line in lines:
        commands = line.split(' ')
        x_move, y_move = get_direction_vector(commands[0])
        for moves in range(int(commands[1])):
            positions[0][0] += x_move
            positions[0][1] += y_move
            
            for i in range(10):
                if i == 0: continue
                positions[i] = move_tail(positions[i-1], positions[i])
                
            coords = '{x},{y}'.format(x=positions[9][0],y=positions[9][1])
            visited_dictionary[coords] = True

    return len(visited_dictionary.keys())
    
print("Test 1", (main(True) == 13))
print("Answer 1", main())


print("Test 1", (main_2(True) == 36))
print("Answer 1", main_2())
























