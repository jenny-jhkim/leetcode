class Solution {
public:
    bool isSubsequence(string s, string t) {
        if(s.length() == 0 )
            return true;
        int i=0;
        int j=0;

        while(i < t.length() && j < s.length() )
        {
            if(s.at(j) == t.at(i))
            {
                j++;
            }
 
            i++;
        }

        if(j == s.length())
            return true;
        else
            return false;
    }
};