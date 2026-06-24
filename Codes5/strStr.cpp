class Solution {
public:
    int strStr(string haystack, string needle) {
        if(needle.empty()) return 0;
        int h=haystack.length();
        int n=needle.length();
        for (int i=0;i<=h-n;++i){
            if(haystack.substr(i,n)==needle){
                return i;
            }
        }
        return -1;
    }
};
