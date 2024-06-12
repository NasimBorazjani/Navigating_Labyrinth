
import heapq

def initialize():
    coins = [84, 2, 8, 16, 21, 10, 15, 4, 17, 16, 4, 85, 30, 13, 28, 2, 2, 11, 18, 9, 25, 5, 24, 14, 20, 30, 6]
    tax_values = {15: 2, 18: 9, 28: 4, 84: 10, 2: 1, 24: 19, 30: 12, 5: 2, 9: 9, 21: 9, 11: 10, 16: 14, 4: 2, 17: 2, 85: 18, 6: 5, 8: 6, 13: 2, 10: 4, 25: 11, 20: 19, 14: 2}
    target_sum = 309
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
