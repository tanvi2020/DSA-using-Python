from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = Counter(t)
        window = {}

        required = len(need)
        formed = 0

        i = 0
        min_len = float('inf')
        ans = ""

        for j in range(len(s)):

            # expand
            char = s[j]
            window[char] = window.get(char, 0) + 1

            # check if this char is satisfied
            if char in need and window[char] == need[char]:
                formed += 1

            # shrink
            while formed == required:

                # update answer
                if (j - i + 1) < min_len:
                    min_len = j - i + 1
                    ans = s[i:j+1]

                # remove left char
                left_char = s[i]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                i += 1

        return ans
        
        