"""""

    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

"""""

class Solution:
    def __init__(self):
        pass

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # Comienza desde i + 1 para evitar usar el mismo índice
                if nums[j] == target - nums[i]:
                    return [i, j]  # Retorna los índices directamente
                     
instancia = Solution()
result = instancia.twoSum([3, 2, 4], 6)
print(result)  # Salida esperada: [1, 2]  
                     