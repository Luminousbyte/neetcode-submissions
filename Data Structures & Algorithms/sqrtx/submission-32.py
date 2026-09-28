class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        l, r = 0, x//2
        res = 0
        while l<=r:
            mid = (l+r)//2
            if x>mid**2:
                l = mid + 1
                res = mid
            elif x<mid**2:
                r = mid - 1
            else:
                return mid
        return res