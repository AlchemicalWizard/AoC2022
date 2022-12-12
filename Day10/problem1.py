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
    instructions = read_data(test, "./test_input.txt")
    
    cycle_count = 0
    reg = 1
    
    sleep = False
    
    instruction_count = 0
    add_amount = 0
    
    signal_strength_sum = 0
    instruction = instructions[instruction_count]
    
    while instruction_count <= len(instructions) -1:
        
        cycle_count += 1
        
        instruction = instructions[instruction_count]
        if (cycle_count-20) % 40 == 0:
            signal_strength_sum += (reg * cycle_count)
     
        if sleep:
            reg += add_amount
            sleep = False
            instruction_count += 1
        elif instruction.startswith("addx"):
            add_amount = int(instruction.split(" ")[1])
            sleep = True
        elif instruction.startswith("noop"):
            instruction_count += 1
            
    return signal_strength_sum

def main_2(test=False):
    instructions = read_data(test, "./test_input2.txt")
    
    cycle_count = 0
    reg = 1
    
    sleep = False
    
    instruction_count = 0
    add_amount = 0
    
    instruction = instructions[instruction_count]
    
    crt_screen = ""
    
    while instruction_count <= len(instructions) -1:
        if (cycle_count%40) >= reg-1 and (cycle_count%40) <= reg + 1:
            crt_screen += '#'
        else: crt_screen += '.'
        
        cycle_count += 1
        
        
        instruction = instructions[instruction_count]
     
        if sleep:
            reg += add_amount
            sleep = False
            instruction_count += 1
        elif instruction.startswith("addx"):
            add_amount = int(instruction.split(" ")[1])
            sleep = True
        elif instruction.startswith("noop"):
            instruction_count += 1
            
        if cycle_count%40 == 0:
            crt_screen += '\n'
    
    return crt_screen

print("Test 1", (main(True) == 13140))
print("Answer 1", main())

print("Test 2: ", main_2(True) == "##..##..##..##..##..##..##..##..##..##..\n###...###...###...###...###...###...###.\n####....####....####....####....####....\n#####.....#####.....#####.....#####.....\n######......######......######......####\n#######.......#######.......#######.....\n")

print("Answer 2", main_2())