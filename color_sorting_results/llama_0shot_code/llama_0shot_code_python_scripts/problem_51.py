
def sort_it(tubes):
    moves = []
    while True:
        changed = False
        for i in range(len(tubes)):
            for j in range(i+1, len(tubes)):
                if len(tubes[i]) < 8 and len(tubes[j]) < 8 and tubes[i][-1] == tubes[j][-1]:
                    tubes[i].append(tubes[i].pop())
                    tubes[j].append(tubes[j].pop())
                    moves.append((i, j))
                    changed = True
        if not changed:
            break
    return moves

tubes = [['Green', 'Green', 'Red', 'Blue', 'Blue'], 
         ['Blue', 'Green', 'Green', 'Red', 'Red'], 
         ['Red', 'Red', 'Blue', 'Green', 'Blue']]

print(sort_it(tubes))
