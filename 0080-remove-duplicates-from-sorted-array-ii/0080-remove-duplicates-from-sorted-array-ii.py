class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        count=0
        while i < len(nums)-1:
            print("i:", i, nums[i], nums[i+1])
            if nums[i] != nums[i+1] :
                i+=1
            else:
                if i < len(nums)-2 and nums[i] == nums [i+2]:
                    nums[i+1:]=nums[i+2:]
                    print(nums)
                else:
                    i+=1

        print(nums)
        k = len(nums)
        return k


                


