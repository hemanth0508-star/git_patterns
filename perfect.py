num = int(input("enter the number:"))
s=1
for i in range(2,int(num**0.5)+1):
    if num%i==0:
        s+=i
        s+=num//i
print("yes" if num==s else "no")