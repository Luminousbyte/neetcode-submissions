class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lst = [0] * len(temperatures)
        stack = []
        for ind, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                j = stack.pop()
                lst[j] = ind - j
            stack.append(ind)
        return lst