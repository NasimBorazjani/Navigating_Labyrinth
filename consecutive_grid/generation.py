
import numpy as np
import random
import random

def generate_3_grid(lower_range, upper_range, num_to_mask, seed):
    grid_generated = False
    while not grid_generated:
        np.random.seed(seed)
        random.seed(seed)

        try:
            # Generate a list of unique random numbers
            numbers = random.sample(range(lower_range, upper_range), 6)

            # Generate first and third rows
            row1_order = random.choice([-1, 1])
            seed += 1
            random.seed(seed)
            row3_order = random.choice([-1, 1])
            row1 = sorted(numbers[:3], key=lambda x: row1_order * x)
            row3 = sorted(numbers[3:6], key=lambda x: row3_order * x)

            # Generate second row
            row2 = [random.randint(min(row1[i], row3[i])+1, max(row1[i], row3[i])-1) for i in range(3)]
            for i in range(3):
                tries = 10
                while row2[i] in numbers:
                    seed += 1
                    tries -= 1
                    random.seed(seed)
                    row2[i] = random.randint(min(row1[i], row3[i])+1, max(row1[i], row3[i])-1)
                    if tries == 0 and row2[i] in numbers:
                        raise
                    
            tries = 10
            while not all(row2[i] < row2[i+1] for i in range(len(row2)-1)) or all(row2[i] > row2[i+1] for i in range(len(row2)-1)):
                seed += 1
                tries -= 1
                random.seed(seed)
                row2[1] = random.randint(max(min(row2[0], row2[2]), min(row1[1], row3[1])) + 1, min(max(row2[0], row2[2]), max(row1[1], row3[1])) -1)
                if tries == 0 and not all(row2[i] < row2[i+1] for i in range(len(row2)-1)) or all(row2[i] > row2[i+1] for i in range(len(row2)-1)):
                    raise

            # Combine rows into a grid
            grid = [row1, row2, row3]
            grid_generated = True
            
            mask = np.full(9, False)
            mask[:num_to_mask] = True
            np.random.shuffle(mask)
            grid = np.where(mask.reshape(3, 3), 'x', grid)
            
            
        except:
            seed += 1
            seed %= 2**32
        
    return grid



def generate_4_grid(lower_range, upper_range, num_to_mask, seed):
    grid_generated = False
    edge_length = 4
    while not grid_generated:
        np.random.seed(seed)
        random.seed(seed)

        try:
            # Generate a list of unique random numbers
            numbers_row_1_4 = random.sample(range(lower_range, upper_range), 2*edge_length)

            # Generate first and fourth rows
            row1_order = random.choice([-1, 1])
            seed += 1
            random.seed(seed)
            row4_order = random.choice([-1, 1])
            row1 = sorted(numbers_row_1_4[:edge_length], key=lambda x: row1_order * x)
            row4 = sorted(numbers_row_1_4[edge_length:], key=lambda x: row4_order * x)

            # Generate second row
            row2 = [random.randint(min(row1[i], row4[i])+1, max(row1[i], row4[i])-1) for i in range(edge_length)]
            for i in range(edge_length):
                tries = 10
                while row2[i] in numbers_row_1_4:
                    seed += 1
                    tries -= 1
                    random.seed(seed)
                    row2[i] = random.randint(min(row1[i], row4[i])+1, max(row1[i], row4[i])-1)
                    if tries == 0 and row2[i] in numbers_row_1_4:
                        raise
                    
            tries = 30
            while not all(row2[i] < row2[i+1] for i in range(len(row2)-1)) or all(row2[i] > row2[i+1] for i in range(len(row2)-1)):
                seed += 1
                tries -= 1
                random.seed(seed)
                row2[1] = random.randint(max(min(row2[0], row2[3]), min(row1[1], row4[1])) + 1, min(max(row2[0], row2[3]), max(row1[1], row4[1])) -1)
                row2[2] = random.randint(max(min(row2[1], row2[3]), min(row1[2], row4[2])) + 1, min(max(row2[1], row2[3]), max(row1[2], row4[2])) -1)
                if tries == 0 and not all(row2[i] < row2[i+1] for i in range(len(row2)-1)) or all(row2[i] > row2[i+1] for i in range(len(row2)-1)):
                    raise

                    
             # Generate third row
            row3 = [random.randint(min(row2[i], row4[i])+1, max(row2[i], row4[i])-1) for i in range(edge_length)]
            for i in range(edge_length):
                tries = 10
                while row3[i] in numbers_row_1_4 or row3[i] in row2:
                    seed += 1
                    tries -= 1
                    random.seed(seed)
                    row3[i] = random.randint(min(row2[i], row4[i])+1, max(row2[i], row4[i])-1)
                    if tries == 0 and (row3[i] in numbers_row_1_4 or row3[i] in row2):
                        raise
                    
            tries = 30
            while not all(row3[i] < row3[i+1] for i in range(len(row3)-1)) or all(row3[i] > row3[i+1] for i in range(len(row3)-1)):
                seed += 1
                tries -= 1
                random.seed(seed)
                row3[1] = random.randint(max(min(row3[0], row3[3]), min(row2[1], row4[1])) + 1, min(max(row3[0], row3[3]), max(row2[1], row4[1])) -1)
                row3[2] = random.randint(max(min(row3[1], row3[3]), min(row2[2], row4[2])) + 1, min(max(row3[1], row3[3]), max(row2[2], row4[2])) -1)
                if tries == 0 and not all(row3[i] < row3[i+1] for i in range(len(row3)-1)) or all(row3[i] > row3[i+1] for i in range(len(row3)-1)):
                    raise

            # Combine rows into a grid
            grid = [row1, row2, row3, row4]
            grid_generated = True
            
            mask = np.full(edge_length*edge_length, False)
            mask[:num_to_mask] = True
            np.random.shuffle(mask)
            grid = np.where(mask.reshape(edge_length, edge_length), 'x', grid)
            
        except:
            seed += 1
            seed %= 2**32
        
    return grid


def generate(edge_length, lower_range, upper_range, num_to_mask, seed):
    if edge_length == 3:
        return generate_3_grid(lower_range, upper_range, num_to_mask, seed)
    elif edge_length == 4:
        return generate_4_grid(lower_range, upper_range, num_to_mask, seed)
    
#print(generate(4, 9, 49, 7, 1))
