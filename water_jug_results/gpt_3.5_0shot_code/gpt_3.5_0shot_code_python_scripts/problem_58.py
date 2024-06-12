
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
                    queue.append((cost + 1, new_volumes))
    
    return -1

jugs = [59, 20, 21, 62, 61, 60]
target_volumes = [149, 156, 173, 186]

result = pour_water(jugs, target_volumes)
print(result)
