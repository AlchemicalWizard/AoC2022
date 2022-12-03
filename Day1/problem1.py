def read_data():
    file = open('./input.txt', 'r')
    lines = file.readlines()
    
    return lines

def main():
    lines = read_data()
    elf_count = 0;
    calorie_sums = [0]
    
    for line in lines:
        if(line == "\n"):
            elf_count += 1
            calorie_sums.append(0)
        else:
            calorie_sums[elf_count] += int(line)

    return max(calorie_sums)

def main_2():
    lines = read_data()
    elf_count = 0;
    calorie_sums = [0]
    
    for line in lines:
        if(line == "\n"):
            elf_count += 1
            calorie_sums.append(0)
        else:
            calorie_sums[elf_count] += int(line)
        
    max_sum = 0
    for i in range(3):
        max_value = max(calorie_sums)
        max_sum += max_value
        calorie_sums.remove(max_value)
    
    return max_sum


print(main())

print(main_2())