
def is_sorted(tubes):
    return all(all(ball == tubes[0][0] for ball in tube) for tube in tubes)

def sort_it(tubes, moves=[]):
    if is_sorted(tubes):
        return moves
    
    shortest_moves = None
    
    for i in range(3):
        for j in range(3):
            if i != j and tubes[i] and (not tubes[j] or tubes[i][-1] == tubes[j][-1]):
                new_tubes = [tube.copy() for tube in tubes]
                new_tubes[j].append(new_tubes[i].pop())
                new_moves = moves + [(i, j)]
                
                result = sort_it(new_tubes, new_moves)
                
                if result is not None and (shortest_moves is None or len(result) < len(shortest_moves)):
                    shortest_moves = result
    
    return shortest_moves

initial_tubes = [['Red', 'Blue', 'Blue', 'Red'], ['Green', 'Green', 'Blue', 'Blue'], ['Green', 'Green', 'Red', 'Red']]
solution = sort_it(initial_tubes)

print(solution)
