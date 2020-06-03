class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        lsA=[]
        diff=[]
        lsA = [i for i,j in costs]
        diff = [j-i for i,j in costs]
        diff.sort()
            
        return sum(lsA) + sum(diff[:len(diff)//2])
