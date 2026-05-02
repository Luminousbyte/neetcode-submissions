class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            lst = arr[i+1:len(arr)]
            if lst:
                arr[i] = max(lst)
            else:
                arr[i] = -1
        return arr