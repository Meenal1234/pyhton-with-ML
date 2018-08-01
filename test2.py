import time
from sklearn.naive_bayes import GaussianNB
import numpy as np
import pandas as pd
d=pd.read_csv('/root/Desktop/iris.data.csv')
t=np.array(d)
fw=0
to=5
t1=t[fw:to]
t2=t1[0:,0:4]
#print(t2)
#print(t1)
d1=np.array(d)
for i in range(fw,to):
	d1=np.delete(d1,0,0)
f=d1[0:,0:4]
l=d1[0:,4]
#print(f)
#print(l)
#print(d1)
clf=GaussianNB()
trained=clf.fit(f,l)
result=trained.predict([t2[2]])
print(result)
time.sleep(1)
