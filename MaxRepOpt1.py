'''
You are given a string text. You can swap two of the characters in the text.
Return the length of the longest substring with repeated characters. 

Example 1:

Input: text = "ababa"
Output: 3
Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa" with length 3.
Example 2:

Input: text = "aaabaaa"
Output: 6
Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa" with length 6.
Example 3:

Input: text = "aaaaa"
Output: 5
Explanation: No need to swap, longest repeated character substring is "aaaaa" with length is 5.
'''
def maxRepOpt1(text: str) -> int:
    L= len(text)
    if (L==1):
        return 1
    if (L==2):
        return 1 if text[0] != text[1] else 2
    freq=[0]*26    
    left=[1]*L
    right=[1]*L

    for i in range(L):
        c = text[i]
        freq[ord(c)-ord('a')]+=1
        if (i >0 and c==text[i-1]):
            left[i]=left[i-1]+1
    for i in range(L-1,-1,-1):
        c = text[i]
        if (i<L-1 and c == text[i+1]):
            right[i]=right[i+1]+1
    ans = 1
    
    for i in range(0, L,1):
        c = text[i]
        if (i>0 and i<L-1 and c!=text[i-1] and text[i-1]==text[i+1]):
            if (freq[ord(text[i-1])-ord('a')]==left[i-1]+right[i+1]):
                ans = max(ans,freq[ord(text[i-1])-ord('a')])
            else:
                ans = max(ans, left[i-1]+right[i+1]+1)
        else:
            if (freq[ord(text[i])-ord('a')]==left[i]):
                ans =max(ans, left[i])
            elif (freq[ord(text[i])-ord('a')]==right[i]):
                ans =max(ans, right[i])
            else:
                ans = max(ans,left[i]+1,right[i]+1)
    
    return ans

if __name__ == '__main__':
    inputs = ["ababa", "aaabaaa", "aaaaa","acbaaa","aa", "cabc"]
    outputs = [3,6,5,4,2,2]

    for i in range(len(inputs)):
        input=inputs[i]
        output=outputs[i]
        res = maxRepOpt1(input)
        print("input={} result={} expected={} match={}".format(input,res,output,res == output))