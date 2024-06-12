
def move_ball(tubes, from_tube, to_tube):
    """
    Moves a ball from the 'from_tube' to the 'to_tube'.
    """
    ball = tubes[from_tube].pop()
    tubes[to_tube].append(ball)

def next_states(tubes):
    """
    Generates all the possible next states from the current state.
    """
    states = []
    for i in range(len(tubes)):
        for j in range(len(tubes)):
            if i != j and len(tubes[i]) > 0 and len(tubes[j]) < 8:
                new_tubes = [list(tube) for tube in tubes]
                move_ball(new_tubes, i, j)
                states.append((new_tubes, i, j))
    return states

def sort_it(tubes):
    """
    Solves the Sort It game.
    """
    moves = []
    while True:
        correctly_sorted = 0
        for tube in tubes:
            if len(tube) == 0:
                correctly_sorted += 1
            else:
                color = tube[0]
                for ball in tube:
                    if ball != color:
                        break
                else:
                    correctly_sorted += 1
        if correctly_sorted == len(tubes):
            break
        else:
            min_moves = float('inf')
            best_state = None
            for new_tubes, from_tube, to_tube in next_states(tubes):
                new_moves = len(moves) + 1
                if new_moves < min_moves:
                    min_moves = new_moves
                    best_state = (new_tubes, from_tube, to_tube)
            tubes, from_tube, to_tube = best_state
            moves.append((from_tube, to_tube))
    return moves

# Test the function
tubes = [['Red', 'Blue', 'Green', 'Blue', 'Blue'], 
         ['Green', 'Red', 'Green', 'Red', 'Blue'], 
         ['Blue', 'Green', 'Red', 'Red', 'Green']]
print(sort_it(tubes))
