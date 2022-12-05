def read_data():
    file = open('./input.txt', 'r')
    lines = file.readlines()
    
    return lines

def main():
    lines = read_data()
    
    start_index, columns = convert_to_arrays(lines)
    
    for line in lines[start_index+1:]:
        amount_to_move, from_column, to_column = parse_command(line)
        
        for i in range(amount_to_move):
            value = columns[from_column].pop(0)
            columns[to_column].insert(0, value)
    
    tops = [x[0] for x in columns]
    ans = ''
    for top in tops:
        ans += top
        
    return ans

def convert_to_arrays(lines):
    col_length = 4
    col_number = len(lines[0])//col_length
    
    cols = [[]*3 for i in range(col_number)]
    
    for index, row in enumerate(lines):
        if row == '\n': return index, cols
        for i in range(0, col_number):
            row_offset = i * 4
            
            column = row[row_offset: row_offset+4].replace('[', '').replace(']','').replace(' ', '').replace('\n', '')
            if column != '' and column > '9':
                cols[i].append(column)
            
    return 0, cols

def parse_command(line):
    line = line.replace('move ', '').replace(' from ', ',').replace(' to ', ',').replace('\n', '')
    commands = [int(x) for x in line.split(',')]
    return commands[0], commands[1] - 1, commands[2] - 1

def main_2():
    lines = read_data()
    
    start_index, columns = convert_to_arrays(lines)
    
    for line in lines[start_index+1:]:
        amount_to_move, from_column, to_column = parse_command(line)
        
        for i in range(amount_to_move):
            value = columns[from_column].pop(amount_to_move-1 - i)
            columns[to_column].insert(0, value)
    
    tops = [x[0] for x in columns]
    ans = ''
    for top in tops:
        ans += top
        
    return ans

print(main())

print(main_2())