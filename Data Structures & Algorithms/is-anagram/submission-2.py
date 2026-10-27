class Solution:
    def isAnagram(self, n: str, m: str) -> bool:
        if len(n) != len(m):
            return False
        s = {}
        for i in n:
         if i in s:
          s[i]+=1
         else:  
          s[i] = 1

        t = {}
        for j in m:
         if j in t:
          t[j]+=1
         else:  
          t[j] = 1  
        return t == s               

           