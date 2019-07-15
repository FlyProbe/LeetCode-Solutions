class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        start = 0
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    temp_l = r - l + 1
                    if temp_l > max_len:
                        max_len = temp_l
                        start = l
                    l -= 1
                    r += 1
                else:
                    break
            l = i
            r = i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    temp_l = r - l + 1
                    if temp_l > max_len:
                        max_len = temp_l
                        start = l
                    l -= 1
                    r += 1
                else:
                    break
        return s[start: start+max_len]
        
