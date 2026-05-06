class Solution:
    def maxDifference(self, s: str) -> int:
        dictionary = defaultdict(int)
        for string in s:
            dictionary[string] += 1

        lst_even, lst_odd = [], []

        for values in dictionary.values():
            if values%2 == 0:
                lst_even.append(values)
            else:
                lst_odd.append(values)

        if not lst_even or not lst_odd:
            return 0

        odd, even = max(lst_odd), min(lst_even)

        res = odd - even

        return res