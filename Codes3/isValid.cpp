using namespace std;
class Solution {
public:
    bool isValid(string word) {
        string vowels = "AEIOUaeiou";
        bool hasV = false;
        bool hasC = false;
        int n = word.length();
          if (n < 3) {
            return false;
        }
        for(int i = 0; i < n; i++) {
            if (!isalnum(word[i])) {
                return false;
            } 
            if (isalpha(word[i])) {
                if (vowels.find(word[i]) != string::npos) {
                    hasV = true;
                } else {
                    hasC = true;
                }
            }
        }
        return hasV && hasC;
    }
};
