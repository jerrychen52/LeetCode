def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseCodes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        tmpSet = set()
        for word in words:
            code=""
            for i in range(len(word)):
                c = word[i]
                code+=morseCodes[ord(c)-ord('a')]
            
            tmpSet.add(code)
        return len(tmpSet)
        
