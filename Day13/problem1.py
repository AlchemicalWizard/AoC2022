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
    
    number_of_pairs = len(lines)//3
    
    index_sum = 0
    
    for i in range(number_of_pairs):
        pair_offset = i*3
        
        
        a_array, _ = format_array(lines[pair_offset][1:-1])
        b_array, _ = format_array(lines[pair_offset+1][1:-1])
    
        in_order = check_order(a_array, b_array)
        
        if in_order == 1:
            index_sum += i+1
        
    return index_sum

def main_2(test=False):
    lines = read_data(test, "./test_input.txt")
    
    number_of_pairs = len(lines)//3
    
    arrays_to_sort = []
    for i in range(number_of_pairs):
        pair_offset = i*3
        
        a_array, _ = format_array(lines[pair_offset][1:-1])
        b_array, _ = format_array(lines[pair_offset+1][1:-1])
        arrays_to_sort.append(a_array)
        arrays_to_sort.append(b_array)    
    
    sorted_list = [[[2]],[[6]]]
    
    while len(arrays_to_sort) > 0:
        line_to_check = arrays_to_sort.pop()
        
        in_order = 0
        
        for i, sort_to_check in enumerate(sorted_list):    
            in_order = check_order(line_to_check, sort_to_check)
            if in_order == 1:
                sorted_list.insert(i, line_to_check)
                break;
        
        if in_order == 2:
            sorted_list.append(line_to_check)

    divider_1 = sorted_list.index([[2]])+1
    divider_2 = sorted_list.index([[6]])+1
    
    return divider_1 * divider_2

def check_order(a, b):
    a_is_int = isinstance(a, int)
    b_is_int = isinstance(b, int)
    
    if a_is_int and b_is_int:
        if a > b:
            return 2
        if b > a:
            return 1
        return 0
    
    if a_is_int and not b_is_int:
        a = [a]
    elif not a_is_int and b_is_int:
        b = [b]
    
    a_len = len(a)
    b_len = len(b)
    for i in range(a_len):
        a_val = a[i]
        
        if i > b_len - 1:
            return 2
        
        b_val = b[i]
        
        result = check_order(a_val, b_val)
        
        if result == 1:
            return 1
        if result == 2:
            return 2
    
    if a_len < b_len:
        return 1
    
    return 0
    
def format_array(string):
    array = []
    char_index = 0
    string_length = len(string)
    while char_index < string_length:
        char = string[char_index]
        if char == '[':
            sub_array, array_end = format_array(string[char_index+1: -1])
            array.append(sub_array)
            char_index += array_end+1
        elif char == ']':
            break
        elif char != ',':
            #check if more digits
            next_offset = 1
            while(next_offset + char_index < string_length-1):
                next_char = string[char_index+next_offset]
                if next_char != '[' and next_char != ']' and next_char != ',':
                    char += next_char
                else: break
                next_offset += 1
                
            array.append(int(char))
        
        char_index += 1
    
    return array, char_index
        
    
print("Test 1", (main(True)==13))
print("Answer 1", main())

print("Test 1", (main_2(True)==140))
print("Answer 1", main_2())