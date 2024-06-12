
def sort_it(tubes):
    moves = []
    colors = ['Red', 'Green', 'Blue']
    
    def move_ball(from_tube, to_tube):
        moves.append((from_tube, to_tube))
        tubes[to_tube].insert(0, tubes[from_tube].pop(0))
    
    def is_sorted():
        return all(all(ball == colors[i] for ball in tube) for i, tube in enumerate(tubes))
    
    while not is_sorted():
        for i in range(3):
            for j in range(3):
                if i != j:
                    if not tubes[i] or (tubes[j] and tubes[i][0] != tubes[j][0]):
                        move_ball(j, i)
                    elif tubes[i] and tubes[j] and tubes[i][0] == tubes[j][0]:
                        for k in range(3):
                            if k != i and k != j:
                                move_ball(j, k)
                                move_ball(i, j)
                                move_ball(k, i)
    
    return moves

initial_state = [['Green', 'Red', 'Green', 'Red'], ['Blue', 'Blue', 'Red', 'Green'], ['Red', 'Blue', 'Green', 'Blue']]
solution = sort_it(initial_state)
print(solution)
