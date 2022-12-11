puzzle = open('input.txt', 'r').read()


def get_marker_position(distinct_characters):
    stream = puzzle[0:distinct_characters]
    for i, ch in enumerate(puzzle, 1):
        stream = stream[1:] + ch
        if len(set(stream)) == distinct_characters:
            return i


print(f'1: Processed characters before marker: {get_marker_position(distinct_characters=4)}')
print(f'2: Processed characters before start-of-message marker: {get_marker_position(distinct_characters=14)}')