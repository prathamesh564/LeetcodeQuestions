class Solution:
    def nthUglyNumber(self, n: int) -> int:
        d=[0]*n
        d[0]=1
        p2=p3=p5=0
        for i in range(1,n):
            next_2=d[p2]*2
            next_3=d[p3]*3
            next_5=d[p5]*5
            next_min=min(next_2,next_3,next_5)
            d[i]=next_min
            if next_min==next_2:
                p2+=1
            if next_min==next_3:
                p3+=1
            if next_min==next_5:
                p5+=1
        return d[-1]    
