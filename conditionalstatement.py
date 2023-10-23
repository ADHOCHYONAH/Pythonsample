num=int(input("Enter Num  :"))

if num> 0:
    print(f"{num} is a positive")

else:
    print(f"{num} is Negative Number")

Age=int(input("Enter Age to vote:"))
if Age>=18 and Age<=80:
    print("you are eligible to vote")
else:
    print("you cant vote because you are minor")