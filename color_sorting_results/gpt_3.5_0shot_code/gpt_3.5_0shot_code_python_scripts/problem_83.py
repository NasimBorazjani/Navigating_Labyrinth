
def sort_it(tubes):
    moves = []
    
    def move_ball(from_tube, to_tube):
        moves.append((from_tube, to_tube))
        tubes[to_tube].append(tubes[from_tube].pop())
    
    def is_sorted():
        return all(all(ball == tubes[0][0] for ball in tube) for tube in tubes)
    
    while not is_sorted():
        for i in range(3):
            for j in range(3):
                if i != j:
                    if tubes[i] and (not tubes[j] or tubes[i][-1] == tubes[j][-1]):
                        move_ball(i, j)
    
    return moves

tubes = [['Red', 'Green', 'Blue', 'Blue', 'Blue', 'Red'], 
         ['Red', 'Red', 'Green', 'Blue', 'Green', 'Blue'], 
         ['Red', 'Red', 'Green', 'Green', 'Blue', 'Green']]

solution = sort_it(tubes)
print(solution)
