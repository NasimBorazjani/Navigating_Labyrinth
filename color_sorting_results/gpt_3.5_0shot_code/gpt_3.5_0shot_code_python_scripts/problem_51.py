
def sort_it(tubes):
    moves = []
    for color in ['Green', 'Red', 'Blue']:
        for i in range(3):
            while tubes[i][-1] != color:
                for j in range(3):
                    if tubes[j] and tubes[j][-1] == color and tubes[i][-1] != color:
                        moves.append((j, i))
                        tubes[i].append(tubes[j].pop())
    return moves

# Initial state of the tubes
tubes = [['Green', 'Green', 'Red', 'Blue', 'Blue'], ['Blue', 'Green', 'Green', 'Red', 'Red'], ['Red', 'Red', 'Blue', 'Green', 'Blue']]

# Solve the problem
solution = sort_it(tubes)

# Print the solution
print(solution)
