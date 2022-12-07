def read_data(test):
    if test:
        path = './test_input.txt'
    else:
        path = './input.txt'
    file = open(path, 'r')
    lines = file.readlines()
    
    return lines

def main(test=False):
    lines = read_data(test)
        
    file_dict = create_filesize_dict(lines)
    return calculate_answer(file_dict)
    
def main_2(test=False):
    lines = read_data(test)
        
    file_dict = create_filesize_dict(lines)
    return calculate_answer_2(file_dict)

def handle_cd(new_path, current_path):
    if new_path == '..':
        current_path.pop()
    else:
        current_path.append(new_path)
        
    return current_path
        
def concat_path(path):
    string = ''
    for i, p in enumerate(path):
        if i > 1:
            string += '/'
        string += p
    return string

def append_dict(dictionary, key_array, value):
    key = concat_path(key_array)
    if key not in dictionary:
        dictionary[key] = 0
    dictionary[key] += value
    
def create_filesize_dict(lines):
    current_path = []
    file_dict = {}
    
    for line in lines:
        line = line.replace("\n","")
        if line.startswith('$'):
            command = line.split(' ')[1:]
            if command[0] == 'cd':
                current_path = handle_cd(command[1], current_path)
            if  command[0] == 'ls':
                continue
        elif not line.startswith('dir'):
            file_size = int(line.split(' ')[0])
            append_dict(file_dict, current_path, file_size)
            
            
            pop_path = current_path.copy()
            for i in range(len(pop_path)-1):
                pop_path.pop()
                append_dict(file_dict, pop_path, file_size)
                
    return file_dict

def calculate_answer(file_dict):
    size_sum = 0
    
    for key in file_dict:
        dir_size = file_dict[key]
        if  dir_size <= 100000:
            size_sum += dir_size

    return size_sum

def calculate_answer_2(file_dict):
    total_space = 70000000
    required_space = 30000000
    used_space = file_dict['/']
    free_space = total_space - used_space
    space_to_free_up = required_space - free_space
    
    smallest = total_space
    for key in file_dict:
        size = file_dict[key]
        if size < smallest and size > space_to_free_up:
            smallest = size
    
    return smallest

print("Test 1", (main(True) == 95437))
print("Answer 1", main())

print("Test 2", (main_2(True) == 24933642))
print("Answer 2", main_2())