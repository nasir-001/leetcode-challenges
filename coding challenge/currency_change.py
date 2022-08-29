class Currency:
    def __init__(self, denominations):
        self.denominations = denominations
 
    def num_ways(self, amount):
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in self.denominations:
            for i in range(1, amount+1):
                if i >= c:
                    dp[i] += dp[i-c]

        return dp[-1]


    def min_change(self, amount):
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0

        for i in range(len(dp)):
            for c in self.denominations:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[1-c] + 1)

        return dp[-1]