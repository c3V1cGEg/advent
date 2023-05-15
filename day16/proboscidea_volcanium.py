import re


class Valve:
    def __init__(self, name, flow_rate, open_minute):
        self.name = name
        self.flow_rate = flow_rate
        self.open_minute = open_minute



data = [row for row in open('input.txt', 'r').read().split('\n')]
d = re.findall(r'Valve ([A-Z]{2}) has flow rate=(\d+); tunnels lead to valves ([A-Z,\s]*)', data[0])

valves = {}
for row in data:
    valve_data = re.findall(r'Valve ([A-Z]{2}) has flow rate=(\d+); tunnel[s]* lead[s]* to valve[s]* ([A-Z,\s]+)', row)
    valves[valve_data[0][0]] = [int(valve_data[0][1]), valve_data[0][2].split(', ')]



def move(valve_name, minute, valve_seq):
    print(minute)
    if minute == 30:
        return

    valve = valves[valve_name]

    openMinute = None
    incr_minute = 0
    if valve[0] > 0:
        openMinute = minute + 1
        incr_minute = 1
    elif valve[0] == 0:
        openMinute = None

    if openMinute == 30:
        return

    nValve = Valve(valve_name, valve[0], openMinute)
    valve_seq.append(nValve)

    for possible_valve in valve[1]:
        move(possible_valve, minute + 1 + incr_minute, valve_seq)

    valve_seq.pop()


start_valve = 'AA'
move(start_valve, 0, [])


print(valves)
