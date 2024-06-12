
def sort_it(tubes):
    moves = []
    while True:
        from_tube = None
        to_tube = None
        for i in range(len(tubes)):
            if len(tubes[i]) > 0 and (from_tube is None or tubes[i][-1] < tubes[from_tube][-1]):
                from_tube = i
        if from_tube is None:
            break
        for i in range(len(tubes)):
            if i != from_tube and len(tubes[i]) < 9 and tubes[i][-1] >= tubes[from_tube][-1]:
                to_tube = i
                break
        if to_tube is None:
            to_tube = [i for i in range(len(tubes)) if len(tubes[i]) < 9 and tubes[i] == []][0]
        moves.append((from_tube, to_tube))
        tubes[to_tube].append(tubes[from_tube].pop())
    return moves
