class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer, permutation can't exist
        if len(s1) > len(s2):
            return False

        # Frequency arrays for s1 and current window in s2
        s1Count, s2Count = [0] * 26, [0] * 26

        # Build initial frequency counts for:
        # - s1
        # - first window of s2 (same length as s1)
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # Count how many characters (out of 26) have matching frequency
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        # Left pointer of sliding window
        l = 0

        # Start sliding window from right = len(s1)
        for r in range(len(s1), len(s2)):

            # If all 26 characters match, we found a permutation
            if matches == 26:
                return True

            # --------------------
            # STEP 1: Add new character (expand window)
            # --------------------
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1

            # Case 1: After adding, counts match → increase matches
            if s1Count[index] == s2Count[index]:
                matches += 1
            # Case 2: Before adding, they were equal → now broken
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # --------------------
            # STEP 2: Remove left character (shrink window)
            # --------------------
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1

            # Case 1: After removal, counts match → increase matches
            if s1Count[index] == s2Count[index]:
                matches += 1
            # Case 2: Before removal, they were equal → now broken
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            # Move left pointer
            l += 1

        # Final check for last window
        return matches == 26