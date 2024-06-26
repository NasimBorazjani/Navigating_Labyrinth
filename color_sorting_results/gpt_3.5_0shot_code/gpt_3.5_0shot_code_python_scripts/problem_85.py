
def sort_it(tubes):
    def is_sorted(tubes):
        return all(all(ball == tubes[0][0] for ball in tube) for tube in tubes)
    
    def move_ball(tubes, from_tube, to_tube):
        if len(tubes[to_tube]) < 9:
            ball = tubes[from_tube].pop(0)
            tubes[to_tube].insert(0, ball)
            return True
        return False
    
    moves = []
    
    while not is_sorted(tubes):
        for i in range(3):
            for j in range(3):
                if i != j and move_ball(tubes, i, j):
                    moves.append((i, j))
                    break
    
    return moves

# Initial state of the tubes
tubes = [['Blue', 'Green', 'Red', 'Red', 'Blue', 'Red'], 
         ['Green', 'Blue', 'Green', 'Blue', 'Red', 'Green'], 
         ['Blue', 'Red', 'Green', 'Green', 'Blue', 'Red']]

# Solve the 'Sort It' game
solution = sort_it(tubes)
print(solution)
