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
    def __init__(self, heightmap: list[str]):
        """Create a dict of coordinates from the map of trees"""
        self.map = {'x': {}, 'y': {}}
        for x, line in enumerate(heightmap):
            self.map['x'][x] = line
            for y, char in enumerate(line):
                self.map['y'][y] = self.map.get('y').get(y, '') + char

    def get_height(self, x: int, y: int):
        """Return the height of the tree at x, y"""
        return int(self.map['x'][y][x])

    def _visible_from(self, x: int, y: int, direction: Direction, count=False) -> int | bool:
        """
        If count is True, return the number of trees visible from the tree at x, y in the given direction.
        If count is False, return True if the tree at x, y is visible from the given direction.
        """
        target_tree = self.get_height(x, y)
        trees_visible = 0

        # Get a list of all trees in the given direction
        if direction == Direction.LEFT:
            treeline = list(reversed(self.map['x'][y][:x]))
        elif direction == Direction.RIGHT:
            treeline = self.map['x'][y][x+1:]
        elif direction == Direction.UP:
            treeline = list(reversed(self.map['y'][x][:y]))
        elif direction == Direction.DOWN:
            treeline = self.map['y'][x][y+1:]
        else:
            raise ValueError('Invalid direction')

        for tree in treeline:
            trees_visible += 1
            if int(tree) >= target_tree:
                # If the tree is taller than the target tree, it blocks the view
                return trees_visible if count else False
        # If no trees are taller than the target tree, it is visible from this direction
        return trees_visible if count else True

    def visible_from(self, x: int, y: int, direction: Direction, count=False):
        """
        Return True if the tree at x, y is visible from the given direction
        If count is True, return the number of trees visible from the tree at x, y in the given direction.
        """
        return self._visible_from(x, y, direction, count=count)

    def visible_from_all_directions(self, x: int, y: int, count=False) -> list[int | bool]:
        """
        Return a list of directions that the tree at x, y is visible from
        If count is True, return the number of trees visible from the tree at x, y in the given direction.
        """
        return [self.visible_from(x, y, Direction.LEFT, count=count),
                self.visible_from(x, y, Direction.RIGHT, count=count),
                self.visible_from(x, y, Direction.UP, count=count),
                self.visible_from(x, y, Direction.DOWN, count=count)]

    def is_visible(self, x: int, y: int) -> bool:
        """Return True if the tree at x, y is visible from at least one direction"""
        return sum(self.visible_from_all_directions(x, y)) > 0

    @staticmethod
    def scenic_score(tree_distance_list: list[int, int, int, int]) -> int:
        """
        Takes a list of 4 numbers, representing the number of trees visible from the tree at x, y in each direction.
        Returns the product of the numbers in the list.
        """
        return reduce(lambda x, y: x * y, tree_distance_list)


# Initialize the map of all trees
tree_map = TreeMap(puzzle)

# Part 1
# Find the number of trees visible from at least one direction
visible_trees = 0
for x, line in enumerate(puzzle):
    visible_trees += sum(tree_map.is_visible(x, y) for y in range(len(line)))
print(f'1: The number of trees visible from outside the grid: {visible_trees}')


# Part 2
# Find the tree with the highest scenic score
scenic_scores = list()
for x, line in enumerate(puzzle):
    scenic_scores += [tree_map.scenic_score(tree_map.visible_from_all_directions(x, y, count=True))
                      for y in range(len(line))]
print(f'2: The highest scenic score possible for a treehouse: {max(scenic_scores)}')