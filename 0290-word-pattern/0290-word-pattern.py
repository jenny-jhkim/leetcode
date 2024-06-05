class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_dic = {}
        
        s_list = s.split()
        
        if len(s_list) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] in word_dic:
                if word_dic[pattern[i]] != s_list[i]:
                    return False                     
            else: #not in pattern_dic
                #Check: no two different keys in 'pattern' map to the same word
                #For Example - pattern = "abca", s = "dog cat cat dog"
                if s_list[i] in word_dic.values(): 
                    return False
                word_dic[pattern[i]] = s_list[i]
        
        return True     