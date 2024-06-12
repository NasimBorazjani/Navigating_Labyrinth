
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
        
        for i in range(5):
            for j in range(5):
                if i != j:
                    new_volumes = volumes.copy()
                    amount = min(new_volumes[i], jugs[j] - new_volumes[j])
                    new_volumes[i] -= amount
                    new_volumes[j] += amount
                    
                    if tuple(new_volumes) not in visited:
                        queue.append((cost + 1, new_volumes))
    
    return -1

jugs = [44, 128, 127, 85, 40, 125]
target_volumes = [283, 295, 428, 428]

result = pour_water(jugs, target_volumes)
print(result)
