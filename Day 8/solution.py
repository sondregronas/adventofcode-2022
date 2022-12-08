from enum import Enum
from functools import reduce


puzzle = open('input.txt', 'r').read().splitlines()


class Direction(Enum):
    """Enum for the direction of the current command"""
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class TreeMap:
    def __init__(self, heightmap):
        """Create a dict of coordinates from the map of trees"""
        self.map = {'x': {}, 'y': {}}
        for x, line in enumerate(heightmap):
            self.map['x'][x] = line
            for y, char in enumerate(line):
                self.map['y'][y] = self.map.get('y').get(y, '') + char

    def height(self, x, y):
        return int(self.map['x'][y][x])

    def visible_from(self, x, y, direction, count=False):
        """
        Return either the number of trees visible from the tree at x, y in the given direction,
        or 1 or 0 if the tree is visible or not
        """
        target_tree = self.height(x, y)
        if direction == Direction.LEFT:
            treeline = list(reversed(self.map['x'][y][:x]))
        elif direction == Direction.RIGHT:
            treeline = self.map['x'][y][x+1:]
        elif direction == Direction.UP:
            treeline = list(reversed(self.map['y'][x][:y]))
        else:  # Direction.DOWN
            treeline = self.map['y'][x][y+1:]

        trees_visible = 0
        for tree in treeline:
            trees_visible += 1
            if int(tree) >= target_tree:
                return trees_visible if count else 0
        return trees_visible if count else 1

    def visible_directions(self, x, y):
        """Return a list of directions that the tree at x, y is visible from"""
        return [self.visible_from(x, y, Direction.LEFT), self.visible_from(x, y, Direction.RIGHT),
                self.visible_from(x, y, Direction.UP), self.visible_from(x, y, Direction.DOWN)]

    def is_visible(self, x, y):
        """Return True if the tree at x, y is visible from at least one direction"""
        return sum(self.visible_directions(x, y)) > 0

    def scenic_score(self, x, y):
        """Return the scenic score of the tree at x, y"""
        visible_trees = [self.visible_from(x, y, Direction.LEFT, count=True),
                         self.visible_from(x, y, Direction.RIGHT, count=True),
                         self.visible_from(x, y, Direction.UP, count=True),
                         self.visible_from(x, y, Direction.DOWN, count=True)]
        return reduce(lambda x, y: x * y, visible_trees)

# Initialize the map of all trees
tree_map = TreeMap(puzzle)

# Part 1
# Find the number of trees visible from at least one direction
visible_trees = 0
for y, line in enumerate(puzzle):
    visible_trees += sum(tree_map.is_visible(x, y) for x in range(len(line)))
print(f'1: The number of trees visible from outside the grid: {visible_trees}')


# Part 2
# Find the tree with the highest scenic score
scenic_scores = list()
for x, line in enumerate(puzzle):
    scenic_scores += [tree_map.scenic_score(x, y) for y in range(len(line))]
print(f'2: The highest scenic score possible for a treehouse: {max(scenic_scores)}')