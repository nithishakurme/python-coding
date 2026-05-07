from tabulate import tabulate
title=["name","age","department"]
data=[["nithisha",21,"civil"],
      ["ravi",60,"mech"],
      ["arun",50,"it"]]
res=tabulate(data,headers=title,tablefmt="pretty")
print(res)
