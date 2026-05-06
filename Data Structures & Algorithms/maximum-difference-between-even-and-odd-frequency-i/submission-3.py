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
        lst_even.sort()
        lst_odd.sort()

        res = lst_odd.pop() - lst_even.pop(0)

        return res