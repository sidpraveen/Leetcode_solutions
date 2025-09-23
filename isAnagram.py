def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    listS = {}
    listT = {}
   
    for i in range(len(s)):
        listS[s[i]] = 1 + listS.get(s[i], 0)
        listT[t[i]] = 1 + listT.get(t[i], 0)

    return listS == listT