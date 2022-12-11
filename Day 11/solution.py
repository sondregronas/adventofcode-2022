import math
from dataclasses import dataclass

# Modulus_factor is the product of all the divisble_by values for all monkeys
# We need this to reduce the size of the numbers we're working with to avoid overflow
# For now it starts as 1, but we'll multiply it by the divisble_by values for each monkey
# as we instantiate them.
modulus_factor = 1


@dataclass
class Monkey:
    items: list
    operation: str
    divisble_by: int
    if_div_true: int
    if_div_false: int

    items_inspected: int = 0

    def __post_init__(self):
        global modulus_factor
        # Multiply the modulus factor by the divisble_by value in order to get the common modulus
        # This is done to prevent the worry level from getting too high
        modulus_factor *= self.divisble_by

    def inspect(self, div_by_3: bool = True):
        """
        Inspect the items, increasing the count of items inspected and modifying the worry level.
        If div_by_3 is True, then the worry level gets divided by 3.
        We also use a modulus to prevent the worry level from ever getting too high, this is done by
        dividing the worry level by the modulus factor (the product of all the divisble_by values)
        """
        global modulus_factor
        # Increase the count of items inspected
        self.items_inspected += len(self.items)
        # Increase worry level (perform the inspection)
        self.items = [eval(self.operation.replace('old', str(item))) for item in self.items]
        # Relieve stress (decrease worry level; the item survived inspection)
        self.items = [int(item) // (3 if div_by_3 else 1) % modulus_factor for item in self.items]

    def test_item(self, item):
        """
        Test the item to see if it is divisble by the given number.
        Return the item and the target monkey
        """
        target_monkey = self.if_div_true if item % self.divisble_by == 0 else self.if_div_false
        return item, target_monkey

    def throw_item(self, item, target_monkey):
        """
        Throw the item to the target monkey, adding it to the target monkey's items and
        removing it from the current monkey's items
        """
        target_monkey.items.append(item)
        self.items.remove(item)

    def do_shenanigans(self, participating_monkeys: list, div_by_3: bool = True):
        """
        Perform the shenanigans for the current monkey
            Inspect: Inspect the items, increasing the count of items inspected and modifying the worry level
                     (If div_by_3 is True, then the worry level gets divided by 3)
            Test: Test the items to see if they are divisble by the given number
            Throw: Throw the item from the current monkey to the target monkey
        """
        self.inspect(div_by_3=div_by_3)
        while self.items:
            item, target_monkey = self.test_item(self.items[0])
            self.throw_item(item, participating_monkeys[target_monkey])


def monkey_business(rounds: int, participants: list, div_by_3: bool = True) -> int:
    """
    Perform the monkey business for the given number of rounds, with the given participants
    If div_by_3 is True, then the worry level gets divided by 3 after each inspection

    Returns the monkey_business, which is the product of the items inspected by the two most active monkeys
    """
    for _ in range(rounds):
        for monkey in participants:
            monkey.do_shenanigans(participants, div_by_3=div_by_3)
    most_active = sorted(participants, key=lambda monkey: monkey.items_inspected, reverse=True)
    return math.prod([monkey.items_inspected for monkey in most_active[:2]])


def instantiate_monkeys():
    """
    Read the input and instantiate the monkeys from it, returning a list of monkeys
    """
    monkeys = list()
    for monkey in open('input.txt', 'r').read().split('\n\n'):
        items = monkey.split('\n')[1].split('Starting items: ')[1].split(', ')
        operation = monkey.split('\n')[2].split('Operation: new = ')[1]
        divisble_by = int(monkey.split('\n')[3].split('Test: divisible by ')[1])
        true_monkey = int(monkey.split('\n')[4].split('If true: throw to monkey ')[1])
        false_monkey = int(monkey.split('\n')[5].split('If false: throw to monkey ')[1])

        monkeys.append(Monkey(items, operation, divisble_by, true_monkey, false_monkey))
    return monkeys


print(f'1: Level of monkey business after 20 rounds: {monkey_business(20, instantiate_monkeys(), div_by_3=True)}')
print(f'2: Level of monkey business after 10000 rounds: {monkey_business(10000, instantiate_monkeys(), div_by_3=False)}')

