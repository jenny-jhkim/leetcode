class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set1 = set(nums1)
        set2 = set(nums2)
                  
        resultSet = set1.intersection(set2)
        result = list(resultSet)
        result.sort()
            
        return result[0] if len(result) > 0 else -1
                
        