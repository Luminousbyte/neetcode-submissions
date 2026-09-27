class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0

        while i**2 <= x:
            if i**2 == x:
                return i
            i += 1
        return int(i-1)
