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
    monkey_info = read_data(test, "./test_input.txt")
    
    monkeys = format_data(monkey_info) 
    
    number_of_rounds = 20
    
    for i in range(number_of_rounds):
        monkeys = do_round(monkeys)
        
    inspects = []
    for monkey in monkeys.values():
        inspects.append(monkey['inspects'])
    
    answer = max(inspects)
    inspects.remove(answer)
    answer *= max(inspects)
    
    return answer

def main_2(test=False):
    monkey_info = read_data(test, "./test_input.txt")
    
    monkeys = format_data(monkey_info) 
    
    number_of_rounds = 10000
    
    factor = 1
    
    for monkey in monkeys.values():
        factor = factor * monkey['tests'][0]
    
    for i in range(number_of_rounds):
        monkeys = do_round2(monkeys,factor)
        
    inspects = []
    for monkey in monkeys.values():
        inspects.append(monkey['inspects'])
    
    answer = max(inspects)
    inspects.remove(answer)
    answer *= max(inspects)
    
    return answer

def do_round(monkeys):
    for monkey in monkeys.values():
        items = monkey['items']
        operations = monkey['operations']
        tests = monkey['tests']
        monkey['inspects'] += len(items)
        while len(items) > 0:
            item = handle_operation(items.pop(), operations)
            if item % tests[0] == 0:
                monkeys[tests[1]]['items'].append(item)
            else:
                monkeys[tests[2]]['items'].append(item)
    
    return monkeys

def do_round2(monkeys, factor):
    for monkey in monkeys.values():
        items = monkey['items']
        operations = monkey['operations']
        tests = monkey['tests']
        monkey['inspects'] += len(items)
        while len(items) > 0:
            item = handle_operation2(items.pop(), operations, factor)
            if item % tests[0] == 0:
                monkeys[tests[1]]['items'].append(item)
            else:
                monkeys[tests[2]]['items'].append(item)
    
    return monkeys    
    
def handle_operation(item, operations):
    if operations[1] == 'old':
        item = item * item
    elif operations[0] == '*':
        item = item * int(operations[1])
    else:
        item = item + int(operations[1])
        
    return item // 3

def handle_operation2(item, operations, factor):
    if operations[1] == 'old':
        item = item * item
    elif operations[0] == '*':
        item = item * int(operations[1])
    else:
        item = item + int(operations[1])
        
    mod_item = item % factor
    return mod_item

def format_data(monkey_info):
    monkeys_state = {}
    number_of_monkeys = len(monkey_info)//7
    for monkey in range(number_of_monkeys):
        monkey_offset = monkey*7
        items = monkey_info[monkey_offset + 1].split('items: ')[1].split(',')
        for i, item in enumerate(items):
            items[i] = int(item)
            
        operations = monkey_info[monkey_offset+2].split('new = old ')[1].split(' ')
        test_divisible = int(monkey_info[monkey_offset+3].split('divisible by ')[1])
        test_true = monkey_info[monkey_offset+4].split('throw to monkey ')[1]
        test_false = monkey_info[monkey_offset+5].split('throw to monkey ')[1]
        
        monkey_state = {'items': items, 'operations':operations, 'tests': [test_divisible, test_true, test_false], 'inspects': 0 }
    
        monkeys_state[str(monkey)] = monkey_state
    
    return monkeys_state

print("Test 1", (main(True) == 10605))
print("Answer 1", main())

print("Test 2", (main_2(True) == 2713310158))
print("Answer 2", main_2())