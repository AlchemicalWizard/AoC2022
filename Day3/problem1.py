def read_data():
    file = open('./input.txt', 'r')
    lines = file.readlines()
    
    for line in lines:        
        line = line.replace(" ", "").replace("\n", "")
    
    return lines

def main():
    lines = read_data()
    
    match_sum = 0
        
    for line in lines:
        line_length = len(line)
        mid_point = int(line_length/2)
        first_compartment = line[:mid_point]
        second_compartment = line[mid_point:]
            
        match = 0
        for first_char in first_compartment:
            for second_char in second_compartment:
                if (first_char == second_char):
                    match_value = convert(first_char)
                    if (match_value > match):
                        match = match_value
                    break;
                        
        match_sum += match
    return match_sum

def convert(char):
    if(char >= 'A' and char <= 'Z'):
        return ord(char) - 64 + 26
    if(char >= 'a' and char <= 'z'):
        return ord(char) - 96
    return 0
    

def main_2():
    lines = read_data()
    
    groups = int(len(lines)/3)
    
    group_sum = 0
    
    for group in range(groups):
        x_line = lines[group*3]
        y_line = lines[group*3 + 1]
        z_line = lines[group*3+2]
        
        highest_priority = 0
        
        for char in x_line:
            if(y_line.find(char) != -1 and z_line.find(char) != -1):
                if convert(char) > highest_priority:
                    highest_priority = convert(char)
            
        print(highest_priority)
        group_sum += highest_priority
            
    return group_sum

print(main())            

print(main_2())