
def is_sorted(tubes):
    for tube in tubes:
        if len(set(tube)) != 1:
            return False
    return True

def sort_it(tubes, moves=[]):
    if is_sorted(tubes):
        return moves
    
    shortest_moves = None
    for i in range(3):
        for j in range(3):
            if i != j and tubes[i] and len(tubes[j]) < 6:
                new_tubes = [tube.copy() for tube in tubes]
                new_tubes[j].append(new_tubes[i].pop())
                new_moves = moves + [(i, j)]
                result = sort_it(new_tubes, new_moves)
                
                if result is not None and (shortest_moves is None or len(result) < len(shortest_moves)):
                    shortest_moves = result
    
    return shortest_moves

initial_state = [['Red', 'Green', 'Green', 'Blue'], ['Red', 'Green', 'Red', 'Blue'], ['Blue', 'Red', 'Green', 'Blue']]
shortest_moves = sort_it(initial_state)

print(shortest_moves)
