
def sort_it(tubes):
    moves = []
    while True:
        from_tube = None
        to_tube = None
        for i in range(3):
            if tubes[i]:
                color = tubes[i][-1]
                if color not in [tubes[j][-1] for j in range(3) if j != i]:
                    from_tube = i
                    for j in range(3):
                        if (j != i and tubes[j] and tubes[j][-1] == color) or (len(tubes[j]) < 9):
                            to_tube = j
                            break
                    break
        if from_tube is None:
            break
        if to_tube is None:
            for j in range(3):
                if len(tubes[j]) < 9:
                    to_tube = j
                    break
        tubes[to_tube].append(tubes[from_tube].pop())
        moves.append((from_tube, to_tube))
    return moves
