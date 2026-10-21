class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and a < 0 < stack[-1]:    # right-mover meets left-mover
                if stack[-1] < -a:                # top is smaller: it explodes
                    stack.pop()
                    continue
                if stack[-1] == -a:               # equal: both explode
                    stack.pop()
                break                             # a is destroyed
            else:
                stack.append(a)                   # a survived (no collision or won all)

        return stack