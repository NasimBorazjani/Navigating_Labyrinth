
from collections import deque

def pour_water(jugs, target_volumes):
    visited = set()
    queue = deque([(0, [0, 0, 0, 0])])  # (cost, volumes)
    
    while queue:
        cost, volumes = queue.popleft()
        
        if volumes == target_volumes:
            return cost
        
        if tuple(volumes) in visited:
            continue
        
        visited.add(tuple(volumes))
        
        for i in range(len(jugs)):
            for j in range(len(volumes)):
                if volumes[j] + jugs[i] <= target_volumes[j]:
                    new_volumes = volumes[:]
                    new_volumes[j] += jugs[i]
                    queue.append((cost + 1, new_volumes))
    
    return -1

jugs = [12, 88, 148, 87, 143, 131]
target_volumes = [260, 295, 331, 394]

shortest_sequence = pour_water(jugs, target_volumes)
print(shortest_sequence)
