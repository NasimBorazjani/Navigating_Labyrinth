
import heapq

def initialize():
    coins = [22, 14, 13, 18, 2, 5, 14, 26, 28, 9, 20, 26, 11, 29, 2, 15, 13, 11, 28, 12, 14, 6, 3, 25, 12, 24, 4, 28, 27, 10, 20, 6, 8, 7, 37, 18, 3, 10, 27, 20, 21, 8, 11, 13, 5, 19, 4, 2]
    tax_values = {2: 2, 14: 13, 29: 2, 13: 3, 25: 20, 28: 18, 11: 7, 9: 1, 3: 2, 15: 3, 8: 2, 7: 1, 12: 6, 26: 9, 19: 11, 24: 1, 22: 9, 27: 17, 6: 4, 18: 14, 21: 12, 4: 3, 37: 6, 20: 16, 5: 5, 10: 6}
    target_sum = 293
    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0
    queue = [(0, 0, [], (0, 0, 0))]
    return (coins, tax_values, target_sum, visited_costs, queue)

def a_star():
    (coins, tax_values, target_sum, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        (total_value, prev_coin, total_tax) = state
        if (total_value == target_sum):
            return actions
        for coin in coins:
            if ((coin not in actions) and ((total_value + coin) <= target_sum)):
                if (((coin < prev_coin) and ((coin % 2) == 0)) or ((coin >= prev_coin) and ((coin % 2) != 0))):
                    coin_tax = tax_values[coin]
                    new_total_tax = (total_tax + coin_tax)
                    new_state = ((total_value + coin), coin, new_total_tax)
                    new_cost = (g + coin_tax)
                    if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, ((g + new_total_tax), new_cost, (actions + [coin]), new_state))
    return None
print(a_star())
