for x in range(int(input())):
    a,b = map(int,input().split())
    total = []
    if a<b:
        for i in range(a+1,b):
            if i%2==1:
                total.append(i)
        print(sum(total))
    else:
        for i in range(b+1,a):
            if i%2==1:
                total.append(i)
        print(sum(total))
       
    
#second_programme
num = int(input())
if num%2==0:
    print("Even")
else:
    print("Odd")
