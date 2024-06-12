
def sort_it(tubes):
    moves = []
    colors = ['Red', 'Green', 'Blue']
    
    def move_ball(from_tube, to_tube):
        moves.append((from_tube, to_tube))
        tubes[to_tube].append(tubes[from_tube].pop())
    
    def is_sorted():
        return all(all(ball == colors[i] for ball in tube) for i, tube in enumerate(tubes))
    
    while not is_sorted():
        for i in range(3):
            if tubes[i] and tubes[i][-1] != colors[i]:
                for j in range(3):
                    if i != j and (not tubes[j] or tubes[j][-1] != colors[i]) and len(tubes[j]) < 6:
                        move_ball(i, j)
                        break
    
    return moves

initial_state = [['Red', 'Red', 'Blue', 'Green'], ['Blue', 'Green', 'Blue', 'Blue'], ['Red', 'Green', 'Green', 'Red']]
result = sort_it(initial_state)
print(result)
