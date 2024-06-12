
def sort_it(tubes):
    moves = []
    target_tubes = [['Red']*7, ['Blue']*7, ['Green']*7]
    
    for target_tube in target_tubes:
        for color in target_tube:
            for i, tube in enumerate(tubes):
                if color in tube:
                    ball_index = tube.index(color)
                    if tube[ball_index:] != target_tube[:len(tube[ball_index:])]:
                        empty_tube_index = [j for j in range(3) if j != i and len(tubes[j]) < 7][0]
                        moves.append((i, empty_tube_index))
                        tubes[empty_tube_index].append(tubes[i].pop(ball_index))
    
    return moves

initial_state = [['Red', 'Blue', 'Red', 'Red'], ['Blue', 'Green', 'Green', 'Blue'], ['Green', 'Blue', 'Green', 'Red']]
moves = sort_it(initial_state)

print(moves)
