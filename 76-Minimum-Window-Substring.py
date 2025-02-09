class Solution(object):
    def minWindow(self, s, t):
        \\\
        :type s: str
        :type t: str
        :rtype: str
        \\\
        window = [0]*58
        res = \\
        resLen = float('inf')
        for letter in t:
            window[ord(letter) - ord('A')]+=1
        print(window)

        l = 0
        def check(window):
            for c in window:
                if c > 0:
                    return False
            return True

        for r in range(len(s)):
            window[ord(s[r]) - ord('A')]-=1
            while check(window):
                if resLen > r-l+1:
                    resLen = r-l+1
                    res = s[l:r+1]
                window[ord(s[l]) - ord('A')]+=1
                l+=1

        return res


        