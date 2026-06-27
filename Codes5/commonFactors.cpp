class Solution {
public:
    int commonFactors(int a, int b) {
        int x=1;
        if(a%x==0||b%x==0){
            while(a%x==0&&b%x==0){
                x+=1;
            }
        }
        return x;
    }
};
