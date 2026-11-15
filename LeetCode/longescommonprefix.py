class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pref = strs[0] 
        pref_len = len(pref) 

        for s in strs[1:]: 
            while pref != s[0:pref_len]: 
                pref_len -= 1 
                if pref_len == 0:
                    return ""
                
                pref = pref[0:pref_len] 
        
        return pref

sol = Solution().longestCommonPrefix(strs = ["flower","flow","flight"])
print(sol)

# The script gets the first string in the list and reads it's length. After that, it grabs the remaining strings.
# While the first string is different from the sliced one being looped, it reduces their size by 1.
# It keeps going until it reaches their prefix.