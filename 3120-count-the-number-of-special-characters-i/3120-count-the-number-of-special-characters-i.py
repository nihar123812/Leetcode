class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
       word = set(word)
       count = 0
       for ch in word:
        if ch.islower() and ch.upper() in word :
            count +=1
       return count
        
