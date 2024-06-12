
from collections import deque

def sort_it(tubes):
    final_state = [['Red']*3, ['Blue']*3, ['Green']*3]
    queue = deque([(tubes, [])])
    visited = set()
    
    while queue:
        current_tubes, moves = queue.popleft()
        state_key = str(current_tubes)
        
        if state_key not in visited:
            visited.add(state_key)
            
            if current_tubes == final_state:
                return moves
            
            for i in range(len(current_tubes)):
                for j in range(len(current_tubes)):
                    if i != j and len(current_tubes[j]) < 9:
                        new_tubes = [tube[:] for tube in current_tubes]
                        ball = new_tubes[i].pop()
                        new_tubes[j].append(ball)
                        new_moves = moves + [(i, j)]
                        queue.append((new_tubes, new_moves))

    return []

initial_state = [['Red', 'Red', 'Blue', 'Red', 'Blue', 'Green'], 
                 ['Green', 'Red', 'Green', 'Green', 'Blue', 'Blue'], 
                 ['Red', 'Green', 'Blue', 'Red', 'Blue', 'Green']]

print(sort_it(initial_state))
