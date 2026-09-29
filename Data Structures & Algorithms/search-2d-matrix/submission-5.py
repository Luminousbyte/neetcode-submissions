class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            
        def binarysrch(x: list, target: int):
            l, r = 0, len(x)-1
            while l<=r:
                mid = l+(r-l)//2
                if target>x[mid]:
                    l = mid + 1
                elif target<x[mid]:
                    r = mid - 1
                else:
                    return True
            return False

        for i in matrix:
            if i[0]<=target<=i[len(i)-1]:
                return binarysrch(i, target)
        return False