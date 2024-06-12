
def sort_it(tubes):
    moves = []
    colors = ['Red', 'Green', 'Blue']
    
    def is_sorted():
        for tube in tubes:
            if len(set(tube)) != 1:
                return False
        return True
    
    while not is_sorted():
        for i in range(3):
            for j in range(3):
                if i != j:
                    if tubes[i][-1] == colors[j] and len(tubes[j]) < 9:
                        moves.append((i, j))
                        tubes[j].append(tubes[i].pop())
    
    return moves

# Initial state of the tubes
tubes = [['Red', 'Red', 'Blue', 'Red', 'Blue', 'Green'], 
         ['Green', 'Red', 'Green', 'Green', 'Blue', 'Blue'], 
         ['Red', 'Green', 'Blue', 'Red', 'Blue', 'Green']]

# Solve the 'Sort It' game
solution = sort_it(tubes)
print(solution)
