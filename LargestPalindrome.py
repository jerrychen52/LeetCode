def largestPalindrome(self, n: int) -> int:
        if (n==1):
            return 9
        maxInt = int(math.pow(10,n))-1
        minInt = (maxInt+1)//10
        def getPalindrome(n)->int:
            temp =n
            result = 0
            count = 1
            while (temp>0):
                result=result*10+temp%10
                temp=temp//10
                if (result > 0):
                    count*=10
                else:
                    count*=100
            return result*count+result
        for i in range(maxInt,minInt,-1):
            pal = getPalindrome(i)
            print("pal={}".format(pal))
            j = maxInt           
            while (j*j>=pal):                
                if (pal % j==0 and pal // j <=maxInt):
                    print("j={}".format(j))
                    print("pal%j={}".format(pal%j))
                    return pal % 1337
                j-=1
        
        return -1

l = getPalindrome(899)
                
