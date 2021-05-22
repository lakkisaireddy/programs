num,r1,r2=map(int,input().split())
if r1>r2:
    r1,r2=r2,r1
    
while r1<=r2:
    print(num,"X",r1,"=",num*r1)
    r1+=1
