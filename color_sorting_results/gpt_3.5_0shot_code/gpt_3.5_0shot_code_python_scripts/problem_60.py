
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
                if i != j and tubes[i] and (not tubes[j] or tubes[i][0] == tubes[j][0]):
                    move_ball(tubes, i, j)
                    moves.append((i, j))
    
    return moves

tubes = [['Green', 'Red', 'Blue', 'Blue', 'Green'], ['Red', 'Green', 'Blue', 'Red', 'Green'], ['Blue', 'Red', 'Blue', 'Green', 'Red']]
moves = sort_it(tubes)
print(moves)
