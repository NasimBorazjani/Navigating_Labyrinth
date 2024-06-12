
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
                        continue
                    if not tubes[j] or tubes[i][0] == tubes[j][0]:
                        move_ball(i, j)
                    elif tubes[i][0] == colors[colors.index(tubes[j][0]) - 1]:
                        move_ball(j, 3 - i - j)
                    elif tubes[i][0] == colors[colors.index(tubes[j][0]) + 1]:
                        move_ball(j, i)
    
    return moves

initial_state = [['Blue', 'Green', 'Green', 'Blue'], ['Red', 'Blue', 'Green', 'Green'], ['Red', 'Red', 'Red', 'Blue']]
result = sort_it(initial_state)
print(result)
