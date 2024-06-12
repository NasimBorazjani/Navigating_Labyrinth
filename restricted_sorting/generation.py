import random
import math

def generate(num_colors, seed):
    random.seed(seed)
    colors = ["Red", "Blue", "Green", "Yellow", "Black", 
              "White", "Pink", "Purple", "Orange", "Brown",
              "Gray", "Teal", "Cyan", "Magenta", "Lime",
              "Maroon", "Navy", "Olive", "Silver", "Gold",
              "Beige", "Ivory", "Coral", "Indigo", "Violet",
              "Crimson", "Turquoise", "Salmon", "Plum",
              "Lavender", "Tan", "Peach", "Mint", "Sky Blue",
              "Rose", "Slate", "Emerald", "Cerulean",
              "Periwinkle", "Sapphire", "Amethyst", "Mauve",
              "Jade", "Raspberry", "Fuchsia", "Chartreuse", 
              "Auburn", "Scarlet", "Dandelion", "Aquamarine"]
    
    # Create a list of colors
    colors = [colors[i] for i in range(num_colors)]
    num_tubes_full = num_colors - 1
    num_tubes_empty = num_colors - 1
    tube_capacity = num_colors
    
    colors = colors * num_tubes_full
    num_blocks_in_each_tube_final = num_tubes_full 
    
    # Randomly shuffle the colors
    random.shuffle(colors)
    
    # Split the colors into the tubes
    tubes_full = [colors[i::num_tubes_full] for i in range(num_tubes_full)]
    tubes = [[] for _ in range(num_tubes_empty)] + tubes_full
    
    random.shuffle(tubes)
    
    cost_dict = {i:random.randint(1, len(tubes) + 1) for i in range(len(tubes))}
        
    return tubes, tube_capacity, num_tubes_full, cost_dict, num_blocks_in_each_tube_final

"""# Test the function
tubes, tube_capacity = generate(4, 4)
for tube in tubes:
    print(tube)
print(tube_capacity)"""