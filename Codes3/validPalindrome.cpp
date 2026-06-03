using namespace std;
class Solution {
    bool isPalindrome(const string& s,int l,int r){
        while(l<r){
            if(s[l]!=s[r]){
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
public:
    bool validPalindrome(string s) {
        int lef=0;
        int righ=s.length()-1;
        while(lef<righ){
            if(lef < righ && s[lef]!= s[righ] ){
                return isPalindrome(s,lef+1,righ)|| isPalindrome(s, lef, righ - 1);
            }
            lef++;
            righ--;
        }
        return true;
    }
};
