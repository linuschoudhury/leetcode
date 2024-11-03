class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        
        rows=len(accounts)
        arraysum=[0]*rows
        for i in range(rows):
            column=len(accounts[i])
            for j in range(column):
                arraysum[i]+=accounts[i][j]
        print(arraysum)
        largest=0
        for k in range(len(arraysum)):
            if arraysum[k]>largest:
                largest=arraysum[k]
        return largest

