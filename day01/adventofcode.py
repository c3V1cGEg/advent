data = open('adventofcode_input.txt', 'r').read()
elf_bag_calories = [sum([int(elf_bag_item) for elf_bag_item in elf_calories.split('\n')]) for elf_calories in data.split('\n\n')]
print(max(elf_bag_calories))

sum_of_three_top_calorie_bags = sum(sorted(elf_bag_calories, reverse=True)[0:3])
print(sum_of_three_top_calorie_bags)