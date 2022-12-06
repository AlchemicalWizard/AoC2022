def read_data():
    file = open('./input.txt', 'r')
    lines = file.readlines()
    
    return lines

def main(buffer_length, test_data=None):
    if test_data == None:
        line = read_data()[0]
    else: line = test_data
        
    char_buffer = []
    
    for index, char in enumerate(line):
        if len(char_buffer) == buffer_length:
            has_duplicates = check_duplicates(char_buffer)
            if not has_duplicates: return index
            char_buffer.pop(0)

        char_buffer.append(char)
        
    return -1
        
def check_duplicates(array):
    for i, i_val in enumerate(array):
        for j, j_val in enumerate(array):
            if i != j and i_val == j_val:
                return True
            
    return False

print("First Half: \n")
print("test 1 ", main(4, "bvwbjplbgvbhsrlpgdmjqwftvncz"))
print("test 2 ", main(4, "nppdvjthqldpwncqszvftbrmjlhg"))
print("test 3 ", main(4, "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"))
print("test 4 ", main(4, "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"))
print("Answer ", main(4))

print("Second Half: \n")
print("test 1 ", main(14, "mjqjpqmgbljsphdztnvjfqwrcgsmlb"))
print("test 2 ", main(14, "bvwbjplbgvbhsrlpgdmjqwftvncz"))
print("test 3 ", main(14, "nppdvjthqldpwncqszvftbrmjlhg"))
print("test 4 ", main(14, "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"))
print("test 5 ", main(14, "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"))
print("Answer ", main(14,))