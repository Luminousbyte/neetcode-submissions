class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l = 0
        r = minutes
        val = 0
        while r <= len(customers):
            total = 0
            for i in range(l, r):
                if grumpy[i] == 1:
                    total += customers[i]
            val = max(total, val)
            l += 1
            r += 1
        val1 = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                val1 += customers[i]
        print(val, val1)
        return val + val1