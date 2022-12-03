def read_data():
    file = open('./input.txt', 'r')
    lines = file.readlines()
    
    return lines

def main():
    lines = read_data()
    score_count = 0
    
    for line in lines:
        plays = line.split(' ')
        try:
            p1 = convert(plays[0])
            p2 = convert(plays[1])
        except Exception:
            print("invalid p1 or p2: {}".format(line))
            return 0
        
        try: 
            round_score = get_result(p1, p2)
        except TypeError:
            print("invalid p1 {} or p2 {}".format(p1, p2))
            return 0
        
        shape_score = p2
        total_score = round_score + shape_score
        
        score_count += total_score
    
    return score_count

def convert(char):
    char = char.replace('\n','').replace(' ','')
    if(char == "A" or char == "X"):
        return 1
    if(char == "B" or char == "Y"):
        return 2
    if(char == "C" or char == "Z"):
        return 3
    raise Exception('invalid char: ', char)

def get_result(p1, p2):
    if((p1 < p2 or (p2 == 1 and p1 == 3)) and not (p2 == 3 and p1 == 1)):
        return 6
    if(p1 == p2):
        return 3
    if(p1 > p2 or (p2 == 3 and p1 == 1)):
        return 0
    raise Exception('invalid results:', p1, p2)



def main_2():
    lines = read_data()
    score_count = 0
    
    for line in lines:
        plays = line.split(' ')
        try:
            p1 = convert(plays[0])
            p2 = convert(plays[1])
        except Exception:
            print("invalid p1 or p2: {}".format(line))
            return 0
        
        try: 
            round_score = get_result_2(p1, p2)
        except TypeError:
            print("invalid p1 {} or p2 {}".format(p1, p2))
            return 0
        
        score_count += round_score
    
    return score_count

def get_result_2(p1, p2):
    if(p2 == 3):
        round_score = 6
        shape_score = p1 + 1
        if shape_score == 4: shape_score = 1
        
    if(p2 == 2):
        round_score = 3
        shape_score = p1
        
    if(p2 == 1):
        round_score = 0
        shape_score = p1 -1
        if shape_score == 0: shape_score = 3

    return round_score + shape_score

print(main())

print(main_2())