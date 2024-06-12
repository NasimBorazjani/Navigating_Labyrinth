
def sort_it(tubes):
    moves = []
    
    def move_ball(from_tube, to_tube):
        moves.append((from_tube, to_tube))
        tubes[to_tube].insert(0, tubes[from_tube].pop(0))
    
    def is_sorted():
        return all(all(ball == tubes[0][0] for ball in tube) for tube in tubes)
    
    while not is_sorted():
        for i in range(3):
            for j in range(3):
                if i != j:
                    if tubes[i] and (not tubes[j] or tubes[i][0] == tubes[j][0]):
                        move_ball(i, j)
    
    return moves

# Initial state of the tubes
tubes = [['Red', 'Blue', 'Green', 'Green'], ['Blue', 'Red', 'Green', 'Blue'], ['Green', 'Blue', 'Red', 'Red']]

# Solve the 'Sort It' game
solution = sort_it(tubes)

# Print the list of move tuples
print(solution)
