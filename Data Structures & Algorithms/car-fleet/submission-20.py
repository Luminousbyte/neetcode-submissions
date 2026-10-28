class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lst = []
        for p, s in zip(position, speed):
            dist = target - p
            lst.append([dist, s])
        lst.sort()
        # print(lst)

        stack = []
        for i in range(len(lst)):
            time = lst[i][0]/lst[i][1]
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
            
        # print(stack)
        return len(stack)