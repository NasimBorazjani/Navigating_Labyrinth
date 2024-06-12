
def sort_it(tubes):
    def is_sorted(tubes):
        return all(all(ball == tubes[0][0] for ball in tube) for tube in tubes)
    
    def move_ball(tubes, from_tube, to_tube):
        ball = tubes[from_tube].pop(0)
        tubes[to_tube].insert(0, ball)
    
    moves = []
    
    while not is_sorted(tubes):
        for i in range(3):
            for j in range(3):
                if i != j and len(tubes[i]) > 0 and len(tubes[j]) < 8:
                    move_ball(tubes, i, j)
                    moves.append((i, j))
    
    return moves

initial_state = [['Blue', 'Green', 'Blue', 'Red', 'Red'], ['Red', 'Red', 'Blue', 'Green', 'Blue'], ['Green', 'Green', 'Red', 'Blue', 'Green']]
moves = sort_it(initial_state)

print(moves)
