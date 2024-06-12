import random

def generate(min_capacity, max_capacity, num_jugs, max_target_rand, num_targets, seed = 1):
    random.seed(seed)
    while True:

        # Generate random capacities
        capacities = [random.randint(min_capacity, max_capacity) for _ in range(num_jugs)]

        rand_capacity = random.choice(capacities)
        rand_capacity_plus_one = rand_capacity + 1
        capacities.append(rand_capacity_plus_one)
        capacities = list(set(capacities))
        
        # Generate random target amounts, 
        # ensure it is solvable by increasing the target capacity to include the max capacity,
        # the difference between target and max capcacity (can be filled by +1 addition) which is randomized, 
        # and the the jug required to do the +1 addtion
        targets = []
        for _ in range(num_targets):
            target_rand_component = random.randint(0, max_target_rand)
            target = rand_capacity_plus_one + max(capacities) + target_rand_component
            targets.append(target)
        
        targets.sort()
        random.shuffle(capacities)
        
        return capacities, targets
        

"""# Generate 10 solvable water jug problems
for i in range(10):
    capacities, target = generate(1, 100, 5, 50, 2, i)
    print(f'Jug capacities: {capacities}, Target amount: {target}')"""