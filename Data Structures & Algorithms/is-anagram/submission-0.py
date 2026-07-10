class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        b={}

        for i in range(0, len(s)):
            if s[i] in a:
                a[s[i]]+=1
            else:
                a[s[i]]=1
        
        for j in range(0, len(t)):
            if t[j] in b:
                b[t[j]]+=1
            else:
                b[t[j]]=1


        return a==b
        