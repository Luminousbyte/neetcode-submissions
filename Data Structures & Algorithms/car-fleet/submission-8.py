class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lst = []
        for n in range(len(position)):
            dist = target - position[n]
            time = dist/speed[n]
            lst.append([dist, time])
        lst.sort()
        stack = []
        for i in lst:
            if stack and i[1] <= stack[-1]:
                continue
            stack.append(i[1])
        return len(stack)