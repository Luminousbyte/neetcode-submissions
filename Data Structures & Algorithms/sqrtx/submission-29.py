class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0
        while l<=r:
            mid = (l+r)//2
            if x>mid**2:
                l = mid + 1
                res = l
            elif x<mid**2:
                r = mid - 1
            else:
                return mid
        return res-1