class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [];
        setNums1 = set(nums1);
        setNums2 = set(nums2);
              
        for x in setNums2:
            if x in setNums1:
                result.append(x);

        return result                  
                