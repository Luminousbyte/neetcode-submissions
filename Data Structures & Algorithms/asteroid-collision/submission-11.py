class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            while stack and i < 0 and stack[-1] > 0:
                diff = stack[-1] + i
                if diff == 0:
                    stack.pop()
                    i = 0
                if diff < 0:
                    stack.pop()
                if diff > 0:
                    i = 0
            if i:
                stack.append(i)
        return stack