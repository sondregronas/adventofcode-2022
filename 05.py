import re
import time

clue = open('05.txt', 'r').read()
cargo_ship = clue.split('\n\n')[0]
instructions = clue.split('\n\n')[1]
# Create a list for cranes 1-9
crate_stacks = {crane: '' for crane in range(1, 10)}

# Decipher rows of cargo ship and add to crate_stacks, bottom to top
for row in cargo_ship.split('\n'):
    crane = 1
    for i in range(0, len(row), 4):
        if '[' in row[i:i + 3]:
            crate_stacks[crane] = row[i:i + 3][1] + crate_stacks[crane]
        crane += 1
# Create an original copy of crate_stacks
original_stacks = dict(crate_stacks)


# Part 1:
# Decipher instructions and move crates accordingly
start = time.time()
for instruction in instructions.split('\n'):
    # Get relevant numbers from instructions
    amount, stack, target = re.findall(r'\d+', instruction)
    amount, stack, target = int(amount), int(stack), int(target)
    # Move the top crate from assigned stack to the target stack, repeat for the given amount of times
    for _ in range(amount):
        crate_stacks[target] += crate_stacks[stack][-1]
        crate_stacks[stack] = crate_stacks[stack][:-1]

top_text = ''.join([crate_stacks[x][-1] for x in crate_stacks])
print(f'1: The top crates now read: "{top_text}"')
print(f'1: Time taken: {time.time() - start}s')

# Part 2:
# The crane now moves multiple crates at once
crate_stacks = original_stacks
start = time.time()
for instruction in instructions.split('\n'):
    amount, stack, target = re.findall(r'\d+', instruction)
    amount, stack, target = int(amount), int(stack), int(target)
    # Move the top <amount> of crates from assigned stack to the target stack
    crate_stacks[target] += crate_stacks[stack][-amount:]
    crate_stacks[stack] = crate_stacks[stack][:-amount]

top_text = ''.join([crate_stacks[x][-1] for x in crate_stacks])
print(f'2: The top crates now read: "{top_text}"')
print(f'2: Time taken: {time.time() - start}s')