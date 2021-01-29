# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
if(t>=1 and t<=10):
    for i in range(t):
        s=input()
        for i in range(len(s)):
            if(i%2==0):
                print(s[i],end="")
        print(" ",end="")
        for i in range(len(s)):
            if(i%2!=0):
                print(s[i],end="")
        print()