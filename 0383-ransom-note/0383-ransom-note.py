class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict={}
        for ch in magazine:
            if ch in mag_dict:
                mag_dict[ch] += 1
            else:
                mag_dict[ch] = 1
                
        for char in ransomNote:
            print(char)
            print(mag_dict)
            if char in mag_dict and mag_dict[char] > 0:
                mag_dict[char] -= 1      
            else:
                return False
                
        return True
                
            