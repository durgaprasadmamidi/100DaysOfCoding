class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ls1=[]
        ls2=[]
        count=0
        while x>0:
            ls1.append(x%2)
            x//=2
        while y>0:
            ls2.append(y%2)
            y//=2
        if len(ls2)>len(ls1):
            for i in range(len(ls1)):
                if ls1[i] != ls2[i]:
                    count+=1
                end=i
            count+=ls2[end+1:].count(1)
        else:
            for i in range(len(ls2)):
                if ls2[i] != ls1[i]:
                    count+=1
                end=i
            count+=ls1[end+1:].count(1)
        return count
solution = Solution()
print(solution.hammingDistance(4,1))
