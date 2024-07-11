# Homework for Topic 9:

import time

def find_coins_greedy(amount):
    """Finds the coin change using a greedy algorithm."""
    coins = [50, 25, 10, 5, 2, 1]
    change = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            change[coin] = count
            amount -= coin * count
    return change


def find_min_coins(amount):
    """Finds the minimum number of coins for change using dynamic programming."""
    coins = [50, 25, 10, 5, 2, 1]
    min_coins = [0] + [float('inf')] * amount
    coin_count = [{} for _ in range(amount + 1)]

    for x in range(1, amount + 1):
        for coin in coins:
            if coin <= x and min_coins[x - coin] + 1 < min_coins[x]:
                min_coins[x] = min_coins[x - coin] + 1
                coin_count[x] = coin_count[x - coin].copy()
                coin_count[x][coin] = coin_count[x].get(coin, 0) + 1

    return coin_count[amount]


def compare_algorithms(test_amounts):
    """Compares the performance of the greedy and dynamic programming algorithms."""
    greedy_times = []
    dp_times = []

    for amount in test_amounts:
        start_time = time.time()
        find_coins_greedy(amount)
        greedy_times.append(time.time() - start_time)

        start_time = time.time()
        find_min_coins(amount)
        dp_times.append(time.time() - start_time)

    return greedy_times, dp_times


# Example usage and performance comparison
if __name__ == "__main__":
    # Test cases
    print("Greedy algorithm result for 113:", find_coins_greedy(113))
    print("Dynamic programming result for 113:", find_min_coins(113))

    # Amounts to test
    test_amounts = [113, 1000, 10000, 100000]  # Moved here

    # Compare performance
    greedy_times, dp_times = compare_algorithms(test_amounts)
    print("\nPerformance Comparison:")
    for i, amount in enumerate(test_amounts):
        print(f"Amount: {amount}")
        print(f"  Greedy Time: {greedy_times[i]:.6f} seconds")
        print(f"  DP Time:     {dp_times[i]:.6f} seconds")

readme_content = """
## Performance Comparison

**Execution Time**

We compared the execution times of both algorithms for different amounts of change. The results are summarized below:

| Amount | Greedy Time (s) | DP Time (s) |
|---|---|---|
| 113   | 2.1457672119140625e-06 | 5.2928924560546875e-05 |
| 1000  | 0.00             | 0.0009081363677978516   |
| 10000 | 0.00             | 0.00527191162109375    |
| 100000| 1.9073486328125e-06 | 0.05571722984313965   |

**Analysis**

*   **Greedy Algorithm:** This algorithm is very fast and efficient for small to moderately large sums. However, it does not always guarantee the minimum number of coins, depending on the coin denominations.

*   **Dynamic Programming Algorithm:** This algorithm guarantees the minimum number of coins but has higher computational complexity, making it slower for very large sums compared to the greedy algorithm.

**Conclusion**

For smaller amounts, the difference in performance between the two algorithms is negligible. However, for larger sums, the greedy algorithm performs significantly faster, although it may not always provide the optimal solution. The dynamic programming algorithm, while slower, guarantees the optimal solution in terms of the minimum number of coins.
"""

with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
