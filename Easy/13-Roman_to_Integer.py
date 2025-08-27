class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        value = 0
        i = 0
        while i < len(s):
            if (i+1 < len(s)):
                if (d[s[i]] < d[s[i+1]]):
                    value += d[s[i+1]] - d[s[i]]
                    i += 1
                elif(d[s[i]] >= d[s[i+1]]):
                    value += d[s[i]]
            else:
                value += d[s[i]]
            i +=1

                
        return value
