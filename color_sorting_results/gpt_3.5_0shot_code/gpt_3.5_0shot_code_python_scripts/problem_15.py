
def sort_it(tubes):
    moves = []
    
    def move_ball(from_tube, to_tube):
        moves.append((from_tube, to_tube))
        tubes[to_tube].insert(0, tubes[from_tube].pop(0))
    
    def is_sorted():
        return all(len(set(tube)) == 1 for tube in tubes)
    
    while not is_sorted():
        for i in range(3):
            for j in range(3):
                if i != j:
                    if len(tubes[i]) > 0 and (len(tubes[j]) == 0 or tubes[i][0] == tubes[j][0]):
                        move_ball(i, j)
    
    return moves

initial_state = [['Blue', 'Red', 'Red', 'Blue'], ['Green', 'Green', 'Red', 'Red'], ['Green', 'Green', 'Blue', 'Blue']]
moves = sort_it(initial_state)

print(moves)
