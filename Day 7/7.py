n=int(input())
if(n>=1 and n<=1000):
    feed=input()
    arr=[]
    for i in range(n):
        arr.append(int(feed.split()[i]))
    arr.reverse()
    for i in range(n):
        print(arr[i],end=" ")