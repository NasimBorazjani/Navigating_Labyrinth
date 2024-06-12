
# Define the capacities of the jugs and the target volumes for the buckets
jug_capacities = [144, 37, 73, 79, 75, 74]
bucket_volumes = [236, 333, 386]

# Initialize the buckets and the actions
buckets = [0, 0, 0]
actions = []

# Fill the buckets
for i in range(len(buckets)):
    # Sort the jugs by capacity in descending order
    jug_capacities.sort(reverse=True)
    
    while bucket_volumes[i] > sum(buckets):
        # Find the jug with the largest capacity that fits in the remaining space
        for capacity in jug_capacities:
            if bucket_volumes[i] - sum(buckets) >= capacity and buckets[i] + capacity <= bucket_volumes[i]:
                # Add water to the bucket
                buckets[i] += capacity
                actions.append(('+', capacity, i+1))
                break

# Check if the buckets are filled correctly
if buckets == bucket_volumes:
    print(actions)
else:
    print("It's not possible to fill the buckets with the given constraints.")
