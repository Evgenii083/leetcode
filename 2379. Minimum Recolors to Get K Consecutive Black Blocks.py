from typing import Self

# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/

def minimumRecolors(self, blocks: str, k: int) -> int:
    
    operations = 0
    
    for i in range(k):
        if blocks[i] == "W":
            operations+=1
    ans = operations
        
    for i in range(k,len(blocks)):
        if blocks[i-k] == "W":
            operations -= 1
        if blocks[i] == "W":
            operations += 1
        if operations == 0:
            ans = operations    
        else:
            ans = min(ans,operations) 
    return ans         


answer = minimumRecolors(Self,blocks="WBBWWBBWBW",k=7)
# answer = minimumRecolors(Self,blocks="WBWBBBW",k=2)
print(answer)        
        