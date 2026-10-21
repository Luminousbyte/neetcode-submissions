class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in asteroids:
            if stack:
                diff = i + stack[-1]

                if stack[-1] > 0 and i < 0 and diff == 0:
                    stack.pop()

                elif stack[-1] > 0 and i < 0 and diff < 0:
                    while stack and stack[-1] > 0 and i < 0:
                        diff = stack[-1] + i

                        if diff == 0:
                            stack.pop()
                            break

                        elif diff > 0:
                            break

                        else:
                            stack.pop()

                    else:
                        stack.append(i)
                        continue

                    if stack and stack[-1] > 0 and i < 0 and diff > 0:
                        continue

                elif stack[-1] > 0 and i < 0 and diff > 0:
                    continue

                else:
                    stack.append(i)

            else:
                stack.append(i)

        return stack