instructions = [row.split(' ') for row in open('input.txt', 'r').read().split('\n')]
register = 1
memory = []

for instr in instructions:
    if instr[0] == 'noop':
        memory.append(register)
    elif instr[0] == 'addx':
        memory.append(register)
        memory.append(register)
        register += int(instr[1])

result = sum([memory[19 + 40 * i]*(20 + 40 * i) for i in range(0, 6)])
print(result)
# task1: 14320, example: 13140


crt = [''] * 240
register = 1
cycle = -1


def draw_pixel(register, cycle):
    if register - 1 <= cycle % 40 <= register + 1:
        crt[cycle] = '#'
    else:
        crt[cycle] = '.'


for instr in instructions:
    if instr[0] == 'noop':
        cycle += 1
        draw_pixel(register, cycle)
    elif instr[0] == 'addx':
        cycle += 1
        draw_pixel(register, cycle)
        cycle += 1
        draw_pixel(register, cycle)

        register += int(instr[1])

crt_list = list(crt)
print('\n'.join([''.join(crt_list[i:i+40]) for i in range(0, len(crt_list), 40)]))
# task2: PCPBKAPJ
