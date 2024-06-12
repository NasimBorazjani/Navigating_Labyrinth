
def sort_it(tubes):
    moves = []
    while True:
        changed = False
        for i in range(len(tubes)):
            for j in range(len(tubes[i])):
                ball = tubes[i][j]
                for k in range(len(tubes)):
                    if i != k and len(tubes[k]) < 8 and tubes[k][-1] != ball:
                        tubes[k].append(ball)
                        tubes[i] = tubes[i][:j] + tubes[i][j+1:]
                        moves.append((i, k))
                        changed = True
                        break
                if changed:
                    break
            if changed:
                break
        if not changed:
            return moves
