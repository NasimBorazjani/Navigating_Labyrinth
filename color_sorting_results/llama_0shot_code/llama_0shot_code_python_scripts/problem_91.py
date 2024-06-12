
def sort_it(tubes):
    moves = []
    while True:
        tube_from = None
        for i in range(3):
            for j in range(6):
                if tubes[i][j] != tubes[i][0]:
                    tube_from = i
                    break
            if tube_from is not None:
                break
        else:
            break
        tube_to = None
        for i in range(3):
            if tubes[i][0] == tubes[tube_from][0] and len(tubes[i]) < 9:
                tube_to = i
                break
            elif tubes[i][0] == '' and len(tubes[i]) < 9:
                tube_to = i
        if tube_to is None:
            break
        moves.append((tube_from, tube_to))
        tubes[tube_to].append(tubes[tube_from].pop(0))
    return moves
