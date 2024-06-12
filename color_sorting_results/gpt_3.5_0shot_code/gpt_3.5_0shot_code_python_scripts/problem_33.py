
def sort_it(tubes):
    moves = []
    
    def move_ball(from_tube, to_tube):
        moves.append((from_tube, to_tube))
        tubes[to_tube].append(tubes[from_tube].pop())
    
    def is_sorted():
        return all(len(set(tube)) == 1 for tube in tubes)
    
    while not is_sorted():
        for i in range(3):
            for j in range(3):
                if i != j:
                    if not tubes[i] or (tubes[j] and tubes[i][-1] == tubes[j][-1]):
                        continue
                    move_ball(i, j)
    
    return moves

tubes = [['Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Blue', 'Blue'], ['Red', 'Blue', 'Blue', 'Red']]
solution = sort_it(tubes)
print(solution)
