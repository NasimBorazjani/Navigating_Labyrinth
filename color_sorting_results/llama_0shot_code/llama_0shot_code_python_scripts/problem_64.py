
def sort_it(tubes):
    colors = {'Red': 0, 'Blue': 1, 'Green': 2}
    moves = []
    while True:
        changed = False
        for i in range(3):
            for j in range(1, 5):
                if tubes[i][j] != tubes[i][0]:
                    for k in range(3):
                        if k != i and tubes[k][0] == tubes[i][j] and len(tubes[k]) < 8:
                            tubes[k].append(tubes[i].pop(j))
                            moves.append((i, k))
                            changed = True
                            break
                    if changed:
                        break
            if changed:
                break
        if not changed:
            break
    return moves

tubes = [['Red', 'Blue', 'Red', 'Red', 'Red'], ['Blue', 'Blue', 'Blue', 'Green', 'Green'], ['Red', 'Green', 'Green', 'Green', 'Blue']]
print(sort_it(tubes))
