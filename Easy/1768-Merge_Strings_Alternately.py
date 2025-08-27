class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        longIndex = max(len(word1), len(word2))
        newWord = []
        for i in range(longIndex):
            if(i < len(word1)):
                newWord.append(word1[i])
            if(i < len(word2)):
                newWord.append(word2[i])
        
        newWord = ''.join(newWord)
        return newWord
