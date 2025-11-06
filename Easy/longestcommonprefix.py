class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
    
        prefix = min(strs, key=len)

        while len(prefix) > 0:
            counter = 0

            for string in strs:
                if string.startswith(prefix):
                    counter += 1

            if counter == len(strs):
                return prefix

            prefix = prefix[:-1]
        
        return ""