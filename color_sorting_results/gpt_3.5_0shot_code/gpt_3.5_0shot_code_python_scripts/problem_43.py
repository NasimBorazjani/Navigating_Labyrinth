
def sort_it(tubes):
    moves = []
    colors = ['Green', 'Blue', 'Red']
    
    def move_ball(from_tube, to_tube):
        moves.append((from_tube, to_tube))
        tubes[to_tube].insert(0, tubes[from_tube].pop(0))
    
    def is_sorted():
        return all(all(ball == colors[i] for i, ball in enumerate(tube)) for tube in tubes)
    
    while not is_sorted():
        for i in range(3):
            for j in range(3):
                if i != j:
                    if tubes[i] and (not tubes[j] or tubes[i][0] == tubes[j][0]):
                        move_ball(i, j)
    
    return moves

initial_state = [['Green', 'Green', 'Blue', 'Red'], ['Red', 'Blue', 'Green', 'Blue'], ['Green', 'Blue', 'Red', 'Red']]
solution = sort_it(initial_state)
print(solution)
