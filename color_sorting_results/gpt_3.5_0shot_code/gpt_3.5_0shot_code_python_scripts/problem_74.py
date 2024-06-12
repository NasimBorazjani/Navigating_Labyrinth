
def sort_it(tubes):
    moves = []
    colors = ['Red', 'Green', 'Blue']
    
    def is_sorted(tubes):
        for tube in tubes:
            if len(set(tube)) != 1:
                return False
        return True
    
    def move_ball(from_tube, to_tube):
        moves.append((from_tube, to_tube))
        ball = tubes[from_tube].pop(0)
        tubes[to_tube].insert(0, ball)
    
    while not is_sorted(tubes):
        for i in range(3):
            for j in range(3):
                if i != j:
                    if tubes[i] and (not tubes[j] or tubes[i][0] == tubes[j][0]):
                        move_ball(i, j)
    
    return moves

initial_state = [['Green', 'Red', 'Green', 'Red', 'Green'], ['Blue', 'Red', 'Green', 'Blue', 'Green'], ['Red', 'Blue', 'Red', 'Blue', 'Blue']]
result = sort_it(initial_state)
print(result)
