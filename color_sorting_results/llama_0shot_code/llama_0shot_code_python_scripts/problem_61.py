
def sort_it(tubes):
    moves = []
    total_moves = 0
    while True:
        changed = False
        for i in range(len(tubes)):
            for j in range(len(tubes[i])):
                for k in range(i + 1, len(tubes)):
                    if len(tubes[k]) < 8 and tubes[i][j] == tubes[k][-1]:
                        tubes[k].append(tubes[i].pop(j))
                        moves.append((i, k))
                        total_moves += 1
                        changed = True
                        break
                if changed:
                    break
            if changed:
                break
        if not changed:
            break
    return moves, total_moves

tubes = [['Red', 'Green', 'Green', 'Red', 'Blue'], 
         ['Red', 'Blue', 'Green', 'Red', 'Green'], 
         ['Green', 'Blue', 'Blue', 'Blue', 'Red']]

moves, total_moves = sort_it(tubes)
print(f"The shortest list of moves: {moves}")
print(f"The total number of moves: {total_moves}")
