cycles = open('input.txt', 'r').read().split('\n')

# This is a bit of a hack, but it works... The main issue is that the
# we add 241 readings to the list, but we're only supposed to add 240.

x, c = 1, 1
readings = {c: x}  # {cycle: reading}

# The first reading is always 1, so we can skip it.
for cycle in cycles:
    c += 1
    # Store the current reading with the cycle number as a key.
    readings[c] = x
    # If the instruction is 'noop', we can skip it.
    if cycle == 'noop':
        continue
    # Add the value to x, then add a cycle, as addition takes 2 cycles.
    x += int(cycle.split(' ')[1])
    c += 1
    # Add the new cycle to the dictionary.
    readings[c] = x

# Remove the last reading, as it's not supposed to be there. (See above)
# TODO: Find a better way to do this.
readings.pop(c)

# Part 1: Sum the readings at the specified cycles.
read_at = (20, 60, 100, 140, 180, 220)
total = sum(x * v for x, v in readings.items() if x in read_at)
print(f"1: Sum of readings: {total}")

# Part 2: Draw pixels to the screen based on a CRT-clock (cycle) and the value of the reading at that cycle.
crt = ''
crt_width = 40
for cycle, value in enumerate(readings.values(), 0):
    # Add a new line every (crt_width) cycles.
    crt += '\n' if cycle % crt_width == 0 and cycle != 0 else ''
    # Add '#' if the difference between the current value and the previous value is 1. Otherwise, add a ' '.
    # (The cursor of the CRT is 3 pixels wide, so a difference of 1 is the same as being within 3 pixels.)
    crt += '#' if abs(cycle % crt_width - value) <= 1 else ' '

print(f"2: The CRT reads:\n{crt}")