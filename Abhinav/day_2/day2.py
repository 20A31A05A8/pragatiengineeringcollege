"""
a=int(input("enter the lemons"))
if a == 21:
    print("you bring sufficient lemons")
elif 0 <= a < 21:
    print("you need ",21-a,"more lemons")
elif a>21:
    print("extra lemons are ",a-21)
else:
    print("you enter negative")
"""
    
"""a=int(input("enter the year"))
if a%4 and 40 and 400 ==0:
    print("the leap year is",a)
"""
"""
eml="abhinav@gmail.com"
ceml=input("enter the mail")
psw=123456
otp=9876
cpsw=int(input("enter the password"))
cotp=int(input("enter the otp"))
if eml==ceml and psw==cpsw :
    if otp==cotp:
        print("login succesful")
    else:
        print("you entered wrong otp")
else:
    print("login failed")
  

list={"red":1,"blue":2,"green":3}
color=input("enter the color")
print(list[color])





a=5
b=True
if 1==b:
    print("yes")
else:
    print("no")
"""
"""
for a in range(97,122):
        print(chr(a),end=' ')
        
for i in range(65,91):
    if i==65 or i==69 or i==73 or i==79 or i==85:
            print(chr(i),end=' ')
            
for i in range(65,91):
    if i!=65 and i!=69 and i!=73 and i!=79 and i!=85:
            print(chr(i),end=' ')
"""       """     
package=84
data=float(2.0)
calls=3000
msg=100
a=int(input("Enter the day:"))
if a<=package:
    print("Your plan will Expiry in",84-a,"Days")
    tdata=float(input("Enter the data used for today:"))
    print("The",data-tdata,"left")
    tcall=int(input("Enter the call made for today:"))
    print(calls-tcall,")
else:
    print("Your package expired")

"""
"""
for i in range(97,123,2):
    for j in range(97,i+1,2):
        print(chr(i),end=' ')
    print("\n")


for i in range(1,11):
    print(i,"* 10 =",i*10)
    """
rows=int(input())
i=1
while i<=rows:
    j=1
    while j<=i:
        print((i),end=' ')
        j=j+1
    i=i+1
    print(' ')

