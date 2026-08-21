class Solution:
    def findKthSmallest(self, coins, k):

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0

            for r in range(1, len(coins) + 1):

                for group in combinations(coins, r):
                    value = 1

                    for coin in group:
                        value = lcm(value, coin)

                    if value <= x:
                        amount = x // value

                        if r % 2 == 1:
                            total += amount
                        else:
                            total -= amount

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left