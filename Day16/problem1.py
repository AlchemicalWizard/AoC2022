import time
from functools import cache

starting_index = 0
valves = []


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


def main(test=False, time=30, elephant=False):
    global starting_index, valves

    lines = read_data(test, "./test_input.txt")

    valves, starting_index = format_data(lines)

    return get_answer(time, elephant)


def get_answer(start_time, elephant):
    global starting_index

    result = do_move(starting_index, frozenset(), start_time, elephant)
    return result


@cache
def do_move(current_position, current_open, current_time, elephant):
    global starting_index, valves

    key = hash('{}{}{}'.format(current_position, str(current_open), current_time))

    if current_time <= 0:
        if elephant:
            # loop for player once elephant turn over
            result = do_move(starting_index, current_open, 26, False)
            return result
        else:
            return 0

    result = 0
    current_valve = valves[current_position]

    if current_position not in current_open and current_valve[0] > 0:
        new_open = set(current_open)
        new_open.add(current_position)
        released_if_open = (current_time - 1) * current_valve[0]
        result = max(result,
                     released_if_open + do_move(current_position, frozenset(new_open), current_time - 1, elephant))

    for next_valve in current_valve[1]:
        result = max(result, do_move(next_valve, frozenset(current_open), current_time - 1, elephant))

    return result


def format_data(lines):
    valve_ids = []
    valves = []
    for line in lines:
        valve_ids.append(line[6:8])

    for i, line in enumerate(lines):
        line = line.replace(' ', '').replace('s', '')
        flow = int(line[line.find('=') + 1:line.find(';')])
        char_connections = line.split('tunnelleadtovalve')[1].split(',')

        connections = []
        for c in char_connections:
            connections.append(valve_ids.index(c))

        valves.append([flow, connections])

    return valves, valve_ids.index('AA')


# print("Test 1", (main(True) == 1651))
start = time.perf_counter()
print("Answer 1", main(False))
print(f"Completed Execution in {time.perf_counter() - start} seconds")

# print("Test 2", (main(True, 26, True) == 1707))

start = time.perf_counter()
print("Answer 2", main(False, 26, True))
print(f"Completed Execution in {time.perf_counter() - start} seconds")
