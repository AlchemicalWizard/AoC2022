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
    
    visible_grid = [[False]*y_len for i in range(x_len)]

    visible_count = 0
    
    # check row
    for i in range(y_len):
        prev_tree = lines[i][0]
        # check left to right
        for j in range(x_len):
            next_tree = lines[i][j]
            prev_tree, visible_count, visible_grid = check_if_visible(prev_tree, next_tree, i, j, visible_grid, visible_count, x_len-1, y_len-1)
            
            if prev_tree == '9': break
        
        
        prev_tree = lines[i][x_len-1]
        # check right to left
        for j in range(x_len-1,-1,-1):
            next_tree = lines[i][j]
            prev_tree, visible_count, visible_grid = check_if_visible(prev_tree, next_tree, i, j, visible_grid, visible_count, x_len-1, y_len-1)
            
            if prev_tree == '9': break
            
    # check col
    for j in range(x_len):
        prev_tree = lines[0][j]
        # check top to bottom
        for i in range(y_len):
            next_tree = lines[i][j]
            prev_tree, visible_count, visible_grid = check_if_visible(prev_tree, next_tree, i, j, visible_grid, visible_count, x_len-1, y_len-1)
            
            if prev_tree == '9': break
        
        
        prev_tree = lines[y_len - 1][j]
        # check dottom to top
        for i in range(y_len-1,-1,-1):
            next_tree = lines[i][j]
            prev_tree, visible_count, visible_grid = check_if_visible(prev_tree, next_tree, i, j, visible_grid, visible_count, x_len-1, y_len-1)
            
            if prev_tree == '9': break
            
    return visible_count

def check_if_visible(prev_tree, next_tree, i, j, visible_grid, visible_count, i_max, j_max):
    
    # if already visible then skip
    if visible_grid[i][j]:
        if prev_tree >= next_tree:
            next_tree = prev_tree
        return (next_tree, visible_count, visible_grid)
    
    if j == 0 or i == 0 or i == i_max or j == j_max:
        visible_count += 1
        visible_grid[i][j] = True
        return (next_tree, visible_count, visible_grid)
    
    # stop checking row if reached 9 height
    if prev_tree >= next_tree:
        return (prev_tree, visible_count, visible_grid)
    
    visible_count += 1
    visible_grid[i][j] = True
    
    return (next_tree, visible_count, visible_grid)

print("Test 1", (main(True) == 22))
print("Ans: ", main())