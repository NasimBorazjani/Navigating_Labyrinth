
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
                    if not tubes[i] or (tubes[j] and tubes[i][-1] == tubes[j][0]):
                        move_ball(j, i)
                    elif not tubes[j] or (tubes[i] and tubes[j][-1] == tubes[i][0]):
                        move_ball(i, j)
    
    return moves

# Initial state of the tubes
tubes = [['Blue', 'Green', 'Red', 'Red', 'Green', 'Blue'], 
         ['Green', 'Blue', 'Blue', 'Blue', 'Red', 'Red'], 
         ['Green', 'Green', 'Green', 'Blue', 'Red', 'Red']]

result = sort_it(tubes)
print(result)
