
def sort_it(tubes):
    moves = []
    while True:
        source = None
        destination = None
        for i in range(3):
            if tubes[i][0] != tubes[i][len(tubes[i])-1]:
                source = i
                for j in range(3):
                    if tubes[j][0] == tubes[i][len(tubes[i])-1] and len(tubes[j]) < 9:
                        destination = j
                        break
                if destination is not None:
                    break
                else:
                    for j in range(3):
                        if len(tubes[j]) < 9:
                            destination = j
                            break
                    if destination is not None:
                        break
        if source is None and destination is None:
            return moves
        moves.append((source, destination))
        tubes[destination].append(tubes[source].pop())
