class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = len(temperatures) * [0]
        stack = []
        for ind, temp in enumerate(temperatures):
            while stack and temperatures[ind] > stack[-1][0]:
                stacktemp, stackind = stack.pop()
                res[stackind] = ind - stackind
            stack.append((temp, ind))
        return res