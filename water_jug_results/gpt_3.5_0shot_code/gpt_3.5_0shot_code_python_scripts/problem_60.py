
from collections import deque

def pour_water(jugs, buckets):
    visited = set()
    queue = deque([(buckets, [])])

    while queue:
        current_buckets, actions = queue.popleft()

        if current_buckets == [176, 189, 251, 285]:
            return actions

        for i in range(len(jugs)):
            for j in range(len(buckets)):
                if j == 0 or current_buckets[j-1] >= current_buckets[j]:
                    new_buckets = current_buckets.copy()
                    if current_buckets[j] + jugs[i] <= buckets[j]:
                        new_buckets[j] += jugs[i]
                        if tuple(new_buckets) not in visited:
                            queue.append((new_buckets, actions + [('+', jugs[i], j)]))
                            visited.add(tuple(new_buckets))
                    if current_buckets[j] - jugs[i] >= 0:
                        new_buckets[j] -= jugs[i]
                        if tuple(new_buckets) not in visited:
                            queue.append((new_buckets, actions + [('-', jugs[i], j)]))
                            visited.add(tuple(new_buckets))

jugs = [78, 68, 49, 82, 77, 88]
buckets = [176, 189, 251, 285]

actions = pour_water(jugs, buckets)
print(actions)
