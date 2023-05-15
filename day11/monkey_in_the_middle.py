class Monkey:
    def __init__(self, items, operation, dividable_by, div_true_monkey, div_false_monkey):
        self.items = items
        self.operation = operation
        self.dividable_by = dividable_by
        self.div_true_monkey = div_true_monkey
        self.div_false_monkey = div_false_monkey
        self.inspect_count = 0

    def calculate_worry_level(self, old):
        self.inspect_count += 1
        return eval(self.operation)


def read_monkey_configuration():
    monkeys_to_play = []
    monkeys = [monkey.split('\n') for monkey in open('input.txt', 'r').read().split('\n\n')]
    for monkey in monkeys:
        items = [int(item.strip()) for item in monkey[1][monkey[1].find(':') + 1:].strip().split(',')]
        monkey_operation = monkey[2][monkey[2].find(':') + 1:].strip()
        operation = monkey_operation[monkey_operation.find('=') + 1:].strip()
        dividable_by = int(monkey[3].split(' ')[-1])
        div_true_monkey = int(monkey[4].split(' ')[-1])
        div_false_monkey = int(monkey[5].split(' ')[-1])
        monkeys_to_play.append(Monkey(items, operation, dividable_by, div_true_monkey, div_false_monkey))
    return monkeys_to_play


def let_monkeys_play_around_task_1(rounds, monkeys_to_play):
    for i in range(0, rounds):
        for monkey in monkeys_to_play:
            for item in monkey.items:
                worry_level = int(monkey.calculate_worry_level(item) / 3)
                if worry_level % monkey.dividable_by == 0:
                    monkeys_to_play[monkey.div_true_monkey].items.append(worry_level)
                else:
                    monkeys_to_play[monkey.div_false_monkey].items.append(worry_level)

            monkey.items = []


def let_monkeys_play_around_task_2(rounds, monkeys_to_play, product):
    for i in range(0, rounds):
        for monkey in monkeys_to_play:
            for item in monkey.items:
                worry_level = int(monkey.calculate_worry_level(item))
                if worry_level > product:
                    worry_level = worry_level % product

                if worry_level % monkey.dividable_by == 0:
                    monkeys_to_play[monkey.div_true_monkey].items.append(worry_level)
                else:
                    monkeys_to_play[monkey.div_false_monkey].items.append(worry_level)

            monkey.items = []


monkeys_to_play = read_monkey_configuration()
let_monkeys_play_around_task_1(20, monkeys_to_play)
monkey_inspections = [monkey.inspect_count for monkey in monkeys_to_play]
monkey_inspections.sort()
print(monkey_inspections[-1] * monkey_inspections[-2])
# task1: 62491, example: 10605

monkeys_to_play = read_monkey_configuration()
product = 1
divs = [monkey.dividable_by for monkey in monkeys_to_play]
for i in divs:
    product *= i

let_monkeys_play_around_task_2(10000, monkeys_to_play, product)
monkey_inspections = [monkey.inspect_count for monkey in monkeys_to_play]
monkey_inspections.sort()
print(monkey_inspections[-1] * monkey_inspections[-2])
# task2: 17408399184, example: 2713310158