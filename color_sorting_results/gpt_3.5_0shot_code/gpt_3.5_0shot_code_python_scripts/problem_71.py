
def sort_it(tubes):
    moves = []
    for color in ['Red', 'Green', 'Blue']:
        for i in range(3):
            while tubes[i] and tubes[i][-1] == color:
                tubes[i].pop()
        for i in range(3):
            while tubes[i] and tubes[i][-1] != color:
                for j in range(3):
                    if i != j and (not tubes[j] or tubes[j][-1] == color or len(tubes[j]) < 8):
                        moves.append((i, j))
                        tubes[j].append(tubes[i].pop())
                        break
    return moves

initial_state = [['Red', 'Blue', 'Blue', 'Blue', 'Green'], ['Red', 'Green', 'Green', 'Red', 'Green'], ['Red', 'Red', 'Blue', 'Green', 'Blue']]
moves = sort_it(initial_state)
print(moves)
