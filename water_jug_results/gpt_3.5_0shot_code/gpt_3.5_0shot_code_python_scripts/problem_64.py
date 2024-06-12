
from queue import Queue

def pour_water(jugs, buckets):
    visited = set()
    q = Queue()
    q.put((0, buckets[:], []))

    while not q.empty():
        current, current_buckets, actions = q.get()

        if current_buckets == [240, 257, 350, 369]:
            return actions

        for i in range(len(jugs)):
            for j in range(len(current_buckets)):
                if j == 0 or current_buckets[j-1] >= current_buckets[j]:
                    new_buckets = current_buckets[:]
                    if current_buckets[j] + jugs[i] <= jugs[i] and current_buckets[j] + jugs[i] <= buckets[j]:
                        new_buckets[j] += jugs[i]
                        if tuple(new_buckets) not in visited:
                            q.put((current+1, new_buckets, actions + [('+', jugs[i], j)]))
                            visited.add(tuple(new_buckets))
                    if current_buckets[j] - jugs[i] >= 0:
                        new_buckets[j] -= jugs[i]
                        if tuple(new_buckets) not in visited:
                            q.put((current+1, new_buckets, actions + [('-', jugs[i], j)]))
                            visited.add(tuple(new_buckets))

jugs = [14, 42, 113, 131, 41, 147]
buckets = [240, 257, 350, 369]

actions = pour_water(jugs, buckets)
print(actions)
