
# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

from typing import List,Self

def findMaxK(self, nums: List[int]) -> int:
    result = -1

    for i in nums:
        for j in nums:
            if i == -j:
                result = max(result, abs(i))

    return result
    
answer = findMaxK(Self,nums=[-1,10,6,7,-7,1])    
print(answer)