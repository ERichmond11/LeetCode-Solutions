class Solution:
    def romanToInt(self, s: str) -> int:
        counter = 0

        for i in range(len(s)-1):
            if (s[i] == 'I' and s[i+1] == 'V'):
                counter-=1
            elif (s[i] == 'I' and s[i+1] == 'X'):
                counter-=1
            elif (s[i] == 'X' and s[i+1] == 'L'):
                counter-=10
            elif (s[i] == 'X' and s[i+1] == 'C'):
                counter-=10
            elif (s[i] == 'C' and s[i+1] == 'D'):
                counter-=100
            elif (s[i] == 'C' and s[i+1] == 'M'):
                counter-=100
            else:
                if s[i] == 'I':
                    counter+=1
                if (s[i] == 'V'):
                    counter+=5
                if s[i] == 'X':
                    counter+=10
                if (s[i] == 'L'):
                    counter+=50
                if s[i] == 'C':
                    counter+=100
                if (s[i] == 'D'):
                    counter+=500
                if (s[i] == 'M'):
                    counter+=1000
        
        if s[-1] == 'I':
            counter+=1
        elif (s[-1] == 'V'):
            counter+=5
        elif s[-1] == 'X':
            counter+=10
        elif (s[-1] == 'L'):
            counter+=50
        elif s[-1] == 'C':
            counter+=100
        elif (s[-1] == 'D'):
            counter+=500
        elif (s[-1] == 'M'):
            counter+=1000

        return counter