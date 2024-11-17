class Solution(object):
    def isHappy(self, n):
        hash=set()
        while n!=1:
            sum=0
            while n>0:
                r=n%10
                sum+=r*r
                n=n//10
            if sum in hash:
                return False
            hash.add(sum)
            n=sum
        if n==1:
            return True
        