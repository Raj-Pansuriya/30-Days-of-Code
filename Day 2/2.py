meal=float(input())
tip=int(input())
tax=int(input())

#round(number,number of digits)
#Rounds the number till specifies number of digit; To integer if nothing is specified

print(round(meal+(tip*meal*0.01)+(tax*meal*0.01)))
