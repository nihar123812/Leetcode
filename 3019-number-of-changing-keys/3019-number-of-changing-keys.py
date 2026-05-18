class Solution:
    def countKeyChanges(self, s: str) -> int:
        count = 0
        x = s.lower()
        y = len(s)
        for i in range(1,y):
            if x[i]!=x[i-1]:
                count+=1
        return count