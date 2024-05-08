
from typing import List, Self

# https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

def averageValue(self, nums: List[int]) -> int:
    array = []

    for i in nums:
        if i%3 ==0 and i%2 ==0:
            array.append(i)
    
    if len(array) > 0:
        return sum(array) // len(array)
    else:
        return 0 
        
result = averageValue(Self,nums=[1,3,6,10,12,15])
print(result)        