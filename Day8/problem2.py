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

def main(test=False):
    lines = read_data(test)
    
    y_len = len(lines)
    x_len = len(lines[0])
    
    max_visibility = 0
    
    # skip edges as will result in 0
    for x in range(1, x_len-1):
        for y in range(1, y_len-1):
            vis = get_visibility(x, y, lines, x_len, y_len)
            if vis > max_visibility: max_visibility = vis
    
    return max_visibility

def get_visibility(x, y, lines, x_len, y_len):
    tree_height = lines[y][x]
    
    down_dist = 0
    for i in range(y+1, y_len):
        down_dist += 1
        if lines[i][x] >= tree_height:
            break
        
    up_dist = 0
    for i in range(y-1, -1, -1):
        up_dist += 1
        if lines[i][x] >= tree_height:
            break
        
    left_dist = 0
    for j in range(x-1, -1, -1):
        left_dist += 1
        if lines[y][j] >= tree_height:
            break
    
    right_dist = 0
    for j in range(x+1, x_len):
        right_dist += 1
        if lines[y][j] >= tree_height:
            break
    
    return (up_dist * down_dist * left_dist * right_dist)

print("Test 1", (main(True) == 8))
print("Ans: ", main())