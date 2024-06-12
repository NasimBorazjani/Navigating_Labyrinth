
def sort_it(tubes):
    moves = []
    while True:
        changed = False
        for i in range(len(tubes)):
            for j in range(len(tubes)):
                if i != j and tubes[j][-1] != tubes[i][-1] and len(tubes[j]) < 8:
                    tubes[j].append(tubes[i].pop())
                    moves.append((i, j))
                    changed = True
        if not changed:
            break
    return moves

tubes = [['Green', 'Red', 'Green', 'Red', 'Green'], 
         ['Blue', 'Red', 'Green', 'Blue', 'Green'], 
         ['Red', 'Blue', 'Red', 'Blue', 'Blue']]

print(sort_it(tubes))
