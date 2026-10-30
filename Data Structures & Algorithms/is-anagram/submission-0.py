class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = [0] * 26
        
        a = ord('a')
        for i in range(len(s)):
            si = ord(s[i]) - a
            ti = ord(t[i]) - a
            counts[si] += 1
            counts[ti] -= 1
        
        for i in range(len(counts)):
            if counts[i] !=0:
                return False

        return True