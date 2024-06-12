import random
import math

#min is 3, max is 50
def generate(num_tubes, tube_capacity, seed):
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
    colors = [colors[i] for i in range(num_tubes)]
    
    #ensure that at least one tube can be completely emptied by moving balls to other tubes
    #num_balls_each_tube = (num_tubes - 1) * (tube_capacity - num_balls_each_tube)
    num_balls_each_tube = math.floor((num_tubes - 1)/num_tubes * tube_capacity)


    colors = colors * num_balls_each_tube
    
    # Randomly shuffle the colors
    random.shuffle(colors)
    
    # Split the colors into the tubes
    tubes = [colors[i::num_tubes] for i in range(num_tubes)]
    
    return tubes
"""
# Test the function
tubes = generate(5, 15, 1)
for tube in tubes:
    print(tube)
print(len(tubes[1]))"""