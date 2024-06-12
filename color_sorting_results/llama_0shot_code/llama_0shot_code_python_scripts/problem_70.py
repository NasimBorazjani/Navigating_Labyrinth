
def sort_it(tubes):
    colors = {'Green': 0, 'Blue': 1, 'Red': 2}
    moves = []
    while True:
        changed = False
        for i in range(3):
            for j in range(3):
                if i != j and len(tubes[i]) > 1 and (len(tubes[j]) == 0 or tubes[j][-1] == tubes[i][-1]):
                    tubes[j].append(tubes[i].pop())
                    moves.append((i, j))
                    changed = True
        if not changed:
            break
    return moves

tubes = [['Green', 'Green', 'Green', 'Red', 'Blue'], ['Blue', 'Blue', 'Red', 'Green', 'Red'], ['Red', 'Green', 'Blue', 'Blue', 'Red']]
tubes = [sorted([colors[color] for color in tube], key=lambda x: (len(tube) - x, x)) for tube in tubes]
print(sort_it(tubes))
