name=input("enter the name:")
sal=int(input("enter salary:"))
desig=input("enter position:")
d={"tl":10,"manager":20,"fresher":5,"developer":15}
tax=sal*[d[desig]/100]
print(tax)
