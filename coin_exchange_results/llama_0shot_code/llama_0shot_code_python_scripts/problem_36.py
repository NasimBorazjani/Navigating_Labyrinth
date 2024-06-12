
import heapq

def taxed_coin_exchange(coins, taxes):
    # Create a list of (value, tax) tuples and sort it
    coins = sorted((value, tax) for value, tax in zip(coins, taxes))
    
    # Initialize the total value and tax
    total_value = total_tax = 0
    
    # Initialize the priority queue
    queue = []
    
    # Initialize the largest coin value used so far
    max_value = 0
    
    # Iterate over the coins in reverse order
    for value, tax in coins[::-1]:
        # If the coin is smaller than the largest coin used so far, skip it
        if value < max_value:
            continue
        # If the coin is larger than or equal to the largest coin used so far,
        # add it to the queue and update the largest coin value
        else:
            heapq.heappush(queue, (value / tax, value))
            max_value = value
    
    # Initialize the result list
    result = []
    
    # While the total value is less than 281
    while total_value < 281:
        # If the queue is empty, break the loop
        if not queue:
            break
        # Pop the coin with the highest value-to-tax ratio from the queue
        _, value = heapq.heappop(queue)
        # Add the value of the coin to the total value and tax
        total_value += value
        total_tax += taxes[value]
        # Add the value of the coin to the result list
        result.append(value)
    
    # Return the result list
    return result

coins = [26, 7, 24, 27, 19, 15, 12, 13, 19, 5, 17, 26, 20, 7, 3, 21, 22, 7, 17, 13, 28, 11, 19, 18, 9, 10, 25, 2, 4, 18, 14, 17, 22, 27, 14, 7, 9, 2, 11, 8, 14, 10, 18, 1, 4, 24, 2, 24, 11, 14, 27]
taxes = {13: 8, 27: 5, 21: 13, 25: 11, 22: 6, 20: 14, 12: 1, 14: 12, 2: 2, 8: 5, 3: 2, 18: 4, 1: 1, 9: 9, 10: 1, 19: 10, 11: 5, 28: 10, 5: 3, 26: 7, 7: 1, 24: 9, 4: 3, 15: 2, 17: 13}

print(taxed_coin_exchange(coins, taxes))
