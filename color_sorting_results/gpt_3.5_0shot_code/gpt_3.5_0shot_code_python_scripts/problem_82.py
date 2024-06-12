
def sort_it(tubes):
    moves = []
    colors = ['Red', 'Green', 'Blue']
    
    def is_sorted():
        return all(all(ball == colors[i] for ball in tube) for i, tube in enumerate(tubes))
    
    def move_ball(from_tube, to_tube):
        moves.append((from_tube, to_tube))
        ball = tubes[from_tube].pop(0)
        tubes[to_tube].insert(0, ball)
    
    while not is_sorted():
        for i in range(3):
            for j in range(3):
                if i != j:
                    if not tubes[i]:
                        for k in range(3):
                            if tubes[k] and tubes[k][0] == colors[i]:
                                move_ball(k, i)
                                break
                    elif tubes[i][0] == colors[j]:
                        move_ball(i, j)
    
    return moves

initial_state = [['Red', 'Green', 'Red', 'Blue', 'Blue', 'Green'], ['Green', 'Green', 'Red', 'Red', 'Blue', 'Blue'], ['Blue', 'Red', 'Green', 'Blue', 'Green', 'Red']]
solution = sort_it(initial_state)
print(solution)
