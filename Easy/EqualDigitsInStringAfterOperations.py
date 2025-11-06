class Solution:
    def hasSameDigits(self, s: str) -> bool:
    
        while (len(s) > 2):
            new_str = ""
            for i in range (len(s)-1):
                sum = (int(s[i]) + int(s[i+1]))% 10
                new_str += str(sum)
            s = new_str
        
        return s[0]==s[1]