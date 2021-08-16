num,n=map(int,input().split())
for i in range(1,n):
    print(num,'*',i,'=',num*i)
    if num*i%2==0:
        print()
