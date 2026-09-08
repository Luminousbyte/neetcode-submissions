class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l = 0
        r = l + minutes - 1
        m_val = 0
        while r < len(customers):
            val = 0
            for i in range(l, r+1):
                if grumpy[i]:
                    val += customers[i]
            m_val = max(val, m_val)
            l += 1
            r += 1

        val = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                val += customers[i]

        return m_val + val
