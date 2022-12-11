# After a days rest, I figured out a better solution to this problem.
# By adding 'addx 0' for every addx <num> instruction, we can force the
# instruction of adding to x to take 2 cycles without extra work.

# We can also replace 'noop' with 'addx 0' to simplify the code, since 'noop' and 'addx 0' just
# indicate that the value of x should be the same as the previous cycle.

instructions = open('input.txt', 'r').read()\
               .replace('addx', 'addx 0\naddx')\
               .replace('noop', 'addx 0')\
               .split('\n')

x, = 1
signal_strength, read_strength_at = 0, (20, 60, 100, 140, 180, 220)
crt, crt_width = '', 40

for cycle, instruction in enumerate(instructions):
    signal_strength += (x * (cycle + 1)) if cycle + 1 in read_strength_at else 0
    crt += ('\n' if cycle % crt_width == 0 and cycle != 0 else '') + \
           ('#' if abs(cycle % crt_width - x) <= 1 else ' ')
    x += int(instruction.split()[1])

print(f"1: Sum of signal strength readings: {signal_strength}")
print(f"2: The CRT reads: \n{crt}")