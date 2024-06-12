
def sort_it(tubes):
    moves = []
    while True:
        from_tube = None
        to_tube = None
        for i in range(3):
            if len(tubes[i]) > 0:
                color = tubes[i][0]
                for j in range(3):
                    if j != i and (len(tubes[j]) == 0 or tubes[j][0] == color) and (len(tubes[j]) < 9):
                        from_tube = i
                        to_tube = j
                        break
                if from_tube is not None and to_tube is not None:
                    break
        if from_tube is None or to_tube is None:
            break
        moves.append((from_tube, to_tube))
        tubes[to_tube].append(tubes[from_tube].pop(0))
    return moves

tubes = [['Red', 'Green', 'Blue', 'Red', 'Red', 'Blue'], 
         ['Green', 'Red', 'Green', 'Green', 'Blue', 'Red'], 
         ['Green', 'Blue', 'Green', 'Blue', 'Blue', 'Red']]

print(sort_it(tubes))
