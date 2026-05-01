a=int(input("enter num 1"))
b=int(input("enter num 2"))
c=int(input("enter num 3"))
if a>b and a>c:
    if b>c:
        print("second largest num is",b)
    else:
        print("second largest num is",c)
elif b>c and b>a:
    if a>c:
        print("second largest num is",a)
    else:
        print("second largest num is",c)
else:
    if a>b:
        print("second largest num is",a)
    else:
        print("second largest num is",b)