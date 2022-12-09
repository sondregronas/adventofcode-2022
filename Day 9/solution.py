instructions = open('input.txt', 'r').readlines()

rope_knots = 10
moves = {"L": (-1, 0), "R": (1, 0), "D": (0, 1), "U": (0, -1)}

# A list of the knots current positions, and a list of the visited positions
knots = [[0, 0] for _ in range(rope_knots)]
visited_knots = [set() for _ in range(rope_knots)]

for instruction in instructions:
    direction, steps = instruction.split()
    for _ in range(int(steps)):
        # Move the head knot first
        knots[0][0] += moves[direction][0]
        knots[0][1] += moves[direction][1]

        # Move child knots, if they are too far away from their parent
        for i, (knot_x, knot_y) in enumerate(knots[1:], 1):
            # Get the spacing between the knot and its parent in both axes
            spacing_x = abs(knots[i-1][0] - knot_x)
            spacing_y = abs(knots[i-1][1] - knot_y)
            # If the knot is more than 1 unit away, move it 1 unit closer to its parent
            if spacing_x > 1 or spacing_y > 1:
                # Get the direction the knot needs to move in
                direction_x = max(-1, min(knots[i-1][0] - knot_x, 1))
                direction_y = max(-1, min(knots[i-1][1] - knot_y, 1))
                # Move the knot
                knots[i][0] += direction_x
                knots[i][1] += direction_y
            else:
                pass  # Knot is already close enough to its parent knot.

            # Add the tail knot to the visited sets in order to get the unique visited knots
            visited_knots[i].add(tuple(knots[i]))

print(f'1: The rope with 2 knots had its tail visiting {len(visited_knots[1])} unique locations.')
print(f'2: The rope with 10 knots had its tail visiting {len(visited_knots[9])} unique locations.')