import matplotlib.pyplot as pyplot
import numpy as np 
overs=np.arange(1,11)
scores=[8,3,6,9,4,5,5,1,2,3]
plt.bar(overs,scores)
plt.title("INDIA SCORE OVER WISE")
plt.xlable("OVER FROM 1 TO 10")
plt.ylabel("RUNS BASED ON OVERS")
plt.xticks(overs)
plt.grid(axis='y',linestyle="__")
plt.show()
