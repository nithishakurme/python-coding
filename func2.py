def sq():
    s=int(input("enter side:"))
    print("area:",s*s)
    
    def clr(r):
        print("area:",r*r*3,14)
        
def rec(a,b):
    print("area:",a*b)
    
while(True):
    print("1.square")
    print("2.circle")
    print("3.rectangle")
    print("4.exit")
    ch=int(input("enter your choice."))
    if ch==1:
        sq()
    elif ch==2:
        clr(20)
    elif ch==3:
        rect(10,20)
    else:
        break
