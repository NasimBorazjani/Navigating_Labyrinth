
import heapq

def initialize():
    coins = [10, 2, 5, 22, 15, 3, 4, 66, 3, 11, 21, 16, 69, 2, 19, 20, 9, 24, 24, 20, 12, 13, 21, 7, 7, 23, 25, 10]
    tax_values = {66: 17, 9: 3, 15: 10, 7: 6, 3: 3, 13: 7, 11: 10, 25: 14, 22: 18, 24: 17, 12: 6, 23: 18, 2: 2, 10: 5, 19: 10, 20: 19, 5: 4, 16: 1, 21: 20, 69: 14, 4: 4}
    target_sum = 268
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
