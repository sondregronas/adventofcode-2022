import re

clue = open('inputs/05.txt', 'r').read()

cargo_ship = clue.split('\n\n')[0]
instructions = clue.split('\n\n')[1]
crate_stacks = {crane: '' for crane in range(1, 10)}

# Decipher rows of cargo ship and add to crate_stacks, bottom to top
for row in cargo_ship.split('\n'):
    crane = 1
    for i in range(0, len(row), 4):
        if '[' == row[i]:
            crate_stacks[crane] = row[i+1] + crate_stacks[crane]
        crane += 1
# Create an original copy of crate_stacks
original_stacks = dict(crate_stacks)


# Part 1:
# Decipher instructions and move crates accordingly
for instruction in instructions.split('\n'):
    # Get relevant numbers from instructions
    amount, stack, target = re.findall(r'\d+', instruction)
    amount, stack, target = int(amount), int(stack), int(target)
    # Move the top crate from assigned stack to the target stack, repeat for the given amount of times
    for _ in range(amount):
        crate_stacks[target] += crate_stacks[stack][-1]
        crate_stacks[stack] = crate_stacks[stack][:-1]
print(f'1: The top crates now read: "{"".join([crate_stacks[x][-1] for x in crate_stacks])}"')


# Part 2:
# The crane now moves multiple crates at once!
crate_stacks = original_stacks
for instruction in instructions.split('\n'):
    amount, stack, target = re.findall(r'\d+', instruction)
    amount, stack, target = int(amount), int(stack), int(target)
    # Move the top <amount> of crates from assigned stack to the target stack
    crate_stacks[target] += crate_stacks[stack][-amount:]
    crate_stacks[stack] = crate_stacks[stack][:-amount]
print(f'2: The top crates now read: "{"".join([crate_stacks[x][-1] for x in crate_stacks])}"')