from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        tCount = Counter(t)
        sCount = Counter()
        have, need = 0, len(tCount)
        res, resLen = [-1, -1], float("inf")
        left = 0

        for right in range(len(s)):
            c = s[right]
            sCount[c] += 1

            if c in tCount and sCount[c] == tCount[c]:
                have += 1

            while have == need:
                # update result
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                # shrink
                sCount[s[left]] -= 1
                if s[left] in tCount and sCount[s[left]] < tCount[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""

