class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            lst = arr[i+1:len(arr)]
            arr[i] = max(lst) if lst else -1
        return arr