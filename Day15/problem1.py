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


def main(test=False, y_to_check=10):
    lines = read_data(test, "./test_input.txt")

    sensors, beacons = format_data(lines)

    return check_coverage(sensors, beacons, y_to_check)


def main_2(test=False, x_max=20, y_max=20):
    lines = read_data(test, "./test_input.txt")

    sensors, beacons = format_data(lines)

    # print_coverage(sensors, beacons)

    for i in range(y_max):
        if i % 10000 == 0:
            print('\n Complete: ', (i * 100 / y_max), '%')
        ret = find_empty(sensors, beacons, i, 0, x_max)
        if ret is not None:
            return (4000000 * ret) + i


def find_empty(sensors, beacons, y_to_check, min_x, max_x):
    ranges = get_covered_ranges(sensors, beacons, y_to_check, min_x, max_x)

    for i, r in enumerate(ranges):
        check_empty = r.stop
        if r.stop >= max_x:
            continue

        found = False
        for j, r2 in enumerate(ranges):
            if i == j:
                continue

            if check_empty in r2:
                found = True

        if not found:
            return check_empty


def check_coverage(sensors, beacons, y_to_check, min_x=-10000000, max_x=10000000):
    ranges = get_covered_ranges(sensors, beacons, y_to_check, min_x, max_x)

    covered = 0
    for r in ranges:
        covered += len(r)

    return covered


def get_covered_ranges(sensors, beacons, y_to_check, min_x, max_x):
    ranges = []
    for i, sensor in enumerate(sensors):
        beacon = beacons[i]
        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        distance_to_check = abs(sensor[1] - y_to_check)
        if distance_to_check <= distance:
            remaining = distance - distance_to_check

            x_minus = sensor[0] - remaining
            x_plus = sensor[0] + remaining

            # put into search range for p2
            x_minus = max([x_minus, min_x])
            x_plus = min([x_plus, max_x])

            new_range = range(x_minus, x_plus)

            found = False

            # optimize by checking if overlapping existing range
            range_counter = 0
            while range_counter < len(ranges):
                r = ranges[range_counter]

                # if encapsulated by another range, don't add
                if new_range.start in r and new_range.stop in r:
                    found = True
                    break

                # if encapsulates another range, overwrite it
                if r.start in new_range and r.stop in new_range:
                    ranges.pop(range_counter)

                    range_counter = 0
                    continue

                # range starts in existing, append existing to left
                if new_range.start in r:
                    new_range = range(r.start, new_range.stop)
                    ranges.pop(range_counter)

                    range_counter = 0
                    continue

                # range ends in existing, append existing to right
                if new_range.stop in r:
                    new_range = range(new_range.start, r.stop)
                    ranges.pop(range_counter)

                    range_counter = 0
                    continue

                range_counter += 1

            if not found:
                ranges.append(new_range)

    return ranges


def format_data(lines):
    sensors = []
    beacons = []

    for line in lines:
        x_splits = line.split('x=')
        comma_index = x_splits[1].find(',')
        sensor_x = int(x_splits[1][:comma_index])
        comma_index = x_splits[2].find(',')
        beacon_x = int(x_splits[2][:comma_index])

        y_splits = line.split('y=')
        colon_index = y_splits[1].find(':')
        sensor_y = int(y_splits[1][:colon_index])
        beacon_y = int(y_splits[2])

        sensors.append([sensor_x, sensor_y])
        beacons.append([beacon_x, beacon_y])
    return sensors, beacons


print("Test 1", (main(True) == 26))
print("Answer 1", main(False, 2000000))

print("Test 1", (main_2(True) == 56000011))
print("Answer 1", main_2(False, 4000000, 4000000))
