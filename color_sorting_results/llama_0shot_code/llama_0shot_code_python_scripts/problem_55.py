
def move(tubes, move):
    src, dest = move
    tubes[dest].append(tubes[src].pop())

def sort_it(initial_tubes):
    tubes = [list(reversed(tube)) for tube in initial_tubes]
    moves = []

    while True:
        changed = False
        for i in range(len(tubes)):
            for j in range(i + 1, len(tubes)):
                if len(tubes[i]) > 0 and len(tubes[j]) > 0 and tubes[i][-1] == tubes[j][-1]:
                    move(tubes, (i, j))
                    moves.append((i, j))
                    changed = True
                    break
            if changed:
                break

        if not changed:
            break

    return list(reversed(moves))

initial_tubes = [['Green', 'Blue', 'Blue', 'Red', 'Red'], ['Green', 'Red', 'Blue', 'Green', 'Green'], ['Red', 'Green', 'Blue', 'Blue', 'Red']]
print(sort_it(initial_tubes))
