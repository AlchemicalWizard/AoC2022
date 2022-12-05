def read_data():
    file = open('./input.txt', 'r')
    lines = file.readlines()
    
    return lines

def main():
    lines = read_data()
    
    pairs = 0
    
    for line in lines:
        
        first_elf_ranges, second_elf_ranges = convert_to_pairs(line)
        
        if (first_elf_ranges[0] >= second_elf_ranges[0] and first_elf_ranges[1] <= second_elf_ranges[1]) or (second_elf_ranges[0] >= first_elf_ranges[0] and second_elf_ranges[1] <= first_elf_ranges[1]):
            pairs +=1
        
    return pairs

def convert_to_pairs(line):
    line = line.replace(" ", "").replace("\n", "")
    elves = line.split(',')
    
    first_elf_ranges = elves[0].split('-')
    first_elf_ranges[0] = int(first_elf_ranges[0])
    first_elf_ranges[1] = int(first_elf_ranges[1])
    second_elf_ranges = elves[1].split('-')
    second_elf_ranges[0] = int(second_elf_ranges[0])
    second_elf_ranges[1] = int(second_elf_ranges[1])
    
    return first_elf_ranges, second_elf_ranges

def main_2():
    lines = read_data()
    
    overlaps = 0
    
    for line in lines:
        first_elf_ranges, second_elf_ranges = convert_to_pairs(line)
        
        if first_elf_ranges[0] >= second_elf_ranges[0] and first_elf_ranges[0] <= second_elf_ranges[1]:
            #elf_1_start inbetween elf_2
            overlaps += 1
            
        elif first_elf_ranges[1] >= second_elf_ranges[0] and first_elf_ranges[1] <= second_elf_ranges[1]:
            #elf_1_end inbetween elf_2
            overlaps +=1
            
        elif second_elf_ranges[0] >= first_elf_ranges[0] and second_elf_ranges[0] <= first_elf_ranges[1]:
            #elf_2_start inbetween elf_1
            overlaps +=1
            
        elif second_elf_ranges[1] >= first_elf_ranges[0] and second_elf_ranges[1] <= first_elf_ranges[1]:
            #elf_2_end inbetween elf_1
            overlaps +=1

    return overlaps


print(main())

print(main_2())