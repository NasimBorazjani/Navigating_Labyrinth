
# Bucket capacities
buckets = [203, 217, 334]

# Jug capacities
jugs = [57, 84, 47, 76, 85, 69]

# Sort jugs in descending order
jugs.sort(reverse=True)

# Initialize actions list
actions = []

# Fill each bucket
for i in range(len(buckets)):
    remaining = buckets[i]
    while remaining > 0:
        for j in range(len(jugs)):
            if remaining >= jugs[j] and (i == len(buckets) - 1 or remaining - jugs[j] >= buckets[i + 1]):
                # Add water to bucket i from jug j
                actions.append(('+', jugs[j], i + 1))
                remaining -= jugs[j]
                break
            elif remaining < jugs[j] and (i == len(buckets) - 1 or remaining < buckets[i + 1]):
                # Add remaining water to bucket i from jug j
                actions.append(('+', remaining, i + 1))
                remaining = 0
                break

# Print actions
print(actions)
