
def perform_move(tubes, move):
    from_tube, to_tube = move
    ball = tubes[from_tube].pop()
    tubes[to_tube].append(ball)

def next_moves(tubes):
    moves = []
    for from_tube in range(len(tubes)):
        for to_tube in range(len(tubes)):
            if from_tube != to_tube and len(tubes[to_tube]) < 8:
                new_tubes = [list(tube) for tube in tubes]
                ball = new_tubes[from_tube].pop()
                new_tubes[to_tube].append(ball)
                if new_tubes not in moves:
                    moves.append((from_tube, to_tube))
    return moves

def sort_it(initial_tubes):
    tubes = [list(tube) for tube in initial_tubes]
    moves = []
    while True:
        sorted_tubes = [['Red']*5, ['Green']*5, ['Blue']*5]
        if tubes == sorted_tubes:
            return moves
        next_moves_list = next_moves(tubes)
        if not next_moves_list:
            return None
        for move in next_moves_list:
            new_tubes = [list(tube) for tube in tubes]
            perform_move(new_tubes, move)
            if new_tubes not in moves:
                moves.append(move)
                tubes = new_tubes
                break

initial_tubes = [['Red', 'Green', 'Blue', 'Red', 'Green'], 
                 ['Green', 'Red', 'Green', 'Red', 'Blue'], 
                 ['Blue', 'Red', 'Green', 'Blue', 'Blue']]

print(sort_it(initial_tubes))
