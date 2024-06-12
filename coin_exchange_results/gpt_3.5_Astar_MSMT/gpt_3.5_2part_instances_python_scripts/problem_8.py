
import heapq

def initialize():
    coins = [4, 17, 8, 15, 6, 14, 2, 4, 16, 10, 6, 5, 14, 8, 18, 2, 17, 9, 17, 59, 3, 10, 21, 4, 9, 14, 14, 20, 14, 8, 14, 18, 5, 16, 14, 17, 5, 3]
    tax_values = {15: 6, 5: 5, 17: 1, 14: 4, 2: 2, 8: 2, 10: 9, 59: 9, 16: 8, 4: 3, 18: 10, 20: 11, 21: 8, 6: 6, 9: 9, 3: 3}
    target_sum = 214
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
