# SAMPLE INPUT:

# 5 2
# 0 1
# 1 1
# 1 2
# 0 1
# 1 1

# SAMPLE OUTPUT:

# 1

# Bessie starts at coordinate 2
# , which is a target of value 1, so she immediately breaks it. She then bounces to coordinate 3, which is a target of value 2, so she can't break it. She continues to coordinate 4, which switches her direction and increases her power by 1 to 2. She bounces back to coordinate 2, which is an already broken target, so she continues. At this point, she bounces to coordinate 0, so she stops. She breaks exactly one target at located at 2

# .

# SAMPLE INPUT:

# 6 4
# 0 3
# 1 1
# 1 2
# 1 1
# 0 1
# 1 1

# SAMPLE OUTPUT:

# 3

length_and_start = list(map(int, input().split()))
length = length_and_start[0]
start = length_and_start[1] - 1

coords = []
for coord in range(length):
    type_and_power = input()
    coords.append([type_and_power[0], type_and_power[1]])


def bessyBouncer(coords, curr_pos):
    targets_broken = 0
    curr_power = 1

    while curr_pos >= 0 and curr_pos < len(coords) and curr_power != 0:
        if coords[curr_pos][0] == 0:
            if curr_power > 0:
                curr_power = -(curr_power + coords[curr_pos][1])
            elif curr_power < 0:
                curr_power = -(curr_power - coords[curr_pos][1])

        elif coords[curr_pos][0] == 1:
            test_power = abs(curr_power)
            if test_power >= coords[curr_pos][1]:
                targets_broken += 1
                coords[curr_pos][0] = 2

        curr_pos += curr_power

    return targets_broken