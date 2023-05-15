# A, X rock 1, B, Y paper 2, C, Z scissors 3
# lost: 0; eq: 3; win: 6
# rock A,X > scissors C,Z; scissors C,Z > paper B,Y; paper B,Y > rock A,X
points = {'X': 1, 'Y': 2, 'Z': 3}
unify = {'A': 'R', 'X': 'R', 'B': 'P', 'Y': 'P', 'C': 'S', 'Z': 'S'}
scoring_combinations = {'SR': 6, 'PS': 6, 'RP': 6, 'RR': 3, 'SS': 3, 'PP': 3}
win_lose_combinations = {'X': {'A': 'Z', 'B': 'X', 'C': 'Y'}, 'Z': {'A': 'Y', 'B': 'Z', 'C': 'X'}, 'Y': {'A': 'X', 'B': 'Y', 'C': 'Z'}}


def play(pair):
    return points[pair[1]] + scoring_combinations.get(unify[pair[0]] + unify[pair[1]], 0)


#Y - draw; X - lose; Z - win
def decrypt(pair):
    return [pair[0], win_lose_combinations.get(pair[1]).get(pair[0])]


print(sum([play(row.split(" ")) for row in open('input.txt', 'r').read().split('\n')]))
#12535 or 15
print(sum([play(decrypt(row.split(" "))) for row in open('input.txt', 'r').read().split('\n')]))
#15457 or 12