
jugs = [(128, 'A'), (67, 'B'), (44, 'C'), (31, 'D'), (127, 'E'), (15, 'F')]
buckets = [258, 261, 415, 430]

# Sort jugs and buckets
jugs.sort()
buckets.sort()

# Initialize the solution
solution = []

# Fill the buckets
for i in range(len(buckets)):
    diff = buckets[i] - (sum(buckets[:i]) if i > 0 else 0)
    for j in range(len(jugs)):
        if jugs[j][0] >= diff:
            solution.append(('+', jugs[j][1], i+1))
            jugs[j] = (jugs[j][0] - diff, jugs[j][1])
            break
        else:
            solution.append(('+', jugs[j][1], i+1))
            diff -= jugs[j][0]
            jugs[j] = (0, jugs[j][1])

print(solution)
