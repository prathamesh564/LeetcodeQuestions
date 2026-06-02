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
        int left=0;
        int right=s.length()-1;
        while(left<right){
            if(left < right && s[left]!= s[right] ){
                return isPalindrome(s,left+1,right)|| isPalindrome(s, left, right - 1);
            }
            left++;
            right--;
        }
        return true;
    }
};
