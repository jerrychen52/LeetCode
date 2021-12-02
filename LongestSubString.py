def findLongestSubString(s:str)->int:
    if (s is None or len(s)==0):
        return 0
    ans = 1
    dictChar = {}
    l=0
    r=0
    while (r<len(s)):
        c = s[r]
        if (not (c in dictChar.keys())):
            dictChar[c]=r
            curLength = r-l+1
            ans = max(ans,curLength)     
            r+=1       
        else:
            l = dictChar[c]+1
            dictChar.pop(c,None)
    
    return ans

print(findLongestSubString("wllqOKgXNRlECQugLEydvjitiwkuXLHQlenaaNvbUtUKWyxhmgTZZSbCDjIEoNLjWMeoWIUskUaVHOlkYlKmYZmSGBjefUPyqZGzkfxaQArDEmJAXRhrfSrvvMWeFYQxZpwBFmPtIkJQBSnKoEDKXcbXfrviDTxqWAkKbjoRAxJfxyNHTnZpqfAUwnEJXnWYlrHXcddrWYlUzSZLEFOGfJCrFIiTFIzQVHRYtZBUOdgGyyrzFiKPviAVT"))