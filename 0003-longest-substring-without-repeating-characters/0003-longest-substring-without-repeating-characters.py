# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         max_len = 0
#         letter = {}
#         sub = ""
        
#         for lett in s:
#             if lett in letter:
#                 max_len = max(len(sub), max_len)
#                 sub = ""
#                 letter.clear()
#                 letter[lett] = letter.get(lett,0) + 1
#                 sub += lett
#             else:
#                 letter[lett] = letter.get(lett,0) + 1
#                 sub += lett
#         # 마지막으로 비교되지 않은 부분 문자열의 길이를 고려
#         max_len = max(len(sub), max_len)
        
#         return max_len
                    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        letter = {}
        start = 0
        
        for i, lett in enumerate(s):
            if lett in letter and letter[lett] >= start:
                start = letter[lett] + 1
            else:
                max_len = max(max_len, i - start + 1)
            letter[lett] = i
        
        return max_len