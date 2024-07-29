class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        count=0
        while i < len(nums)-1:
            print("i:", i, nums[i], nums[i+1])
            if nums[i] != nums[i+1] :
                i+=1
                count = 0
            else:
                count+=1
                if count >=2:
                    nums[i+1:]=nums[i+2:]
                    print(nums)
                else:
                    i+=1
        print(nums)
        k = len(nums)
        return k


                


