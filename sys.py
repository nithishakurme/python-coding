import time
import sys
h=12
m=30
s=0
while True:
    print("{:02d}:{:02d}:{:02d}".format(h,m,s),end="\r")
    time.sleep(1)
    s+=1
    if s==60:
        s=0
        m+=1
    if m==60:
        m=0
        h+=1
    if h==24:
        h=0