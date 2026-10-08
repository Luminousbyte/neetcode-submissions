class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        for t in range(len(position)):
            time.append((target-position[t])/speed[t])
        # print(time)
        lst = []
        for p, t in zip(position, time):
            lst.append([p, t])
        lst.sort()
        # print(lst)

        stack = []
        for i in range(len(lst)):
            while stack and lst[i][1] > stack[-1]:
                stack.pop()
            stack.append(lst[i][1])
        # print(stack)
        return len(set(stack))