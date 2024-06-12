
from collections import deque

def sort_it(tubes):
    final_state = [['Blue']*6, ['Green']*6, ['Red']*6]
    final_state_str = map(str, final_state)
    initial_state_str = map(str, tubes)
    visited = {str(tubes): None}
    q = deque([(tubes, None)])
    while q:
        tubes, prev_move = q.popleft()
        if str(tubes) in final_state_str:
            return prev_move
        for i in range(len(tubes)):
            for j in range(len(tubes)):
                if i != j and len(tubes[j]) < 9:
                    for k in range(len(tubes[i])-1, -1, -1):
                        new_tubes = [t[:] for t in tubes]
                        new_tubes[j].append(new_tubes[i].pop(k))
                        new_tubes_str = map(str, new_tubes)
                        if str(new_tubes) not in visited:
                            visited[str(new_tubes)] = (i, j)
                            q.append((new_tubes, (i, j)))
    return []

tubes = [['Blue', 'Green', 'Red', 'Red', 'Green', 'Blue'], 
         ['Green', 'Blue', 'Blue', 'Blue', 'Red', 'Red'], 
         ['Green', 'Green', 'Green', 'Blue', 'Red', 'Red']]

print(sort_it(tubes))
