from sklearn.preprocessing import OneHotEncoder
import numpy as np
import csv
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import Imputer
from sklearn.ensemble import RandomForestClassifier
import pickle

onehotdata=pickle.load(open('oneHotTotal.pkl'))
df=pd.read_csv('newData.csv')
df1=pd.read_csv('Initial_Test_Data.csv')
tr=df.values
te=df1.values
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
tr=imp.fit(tr).transform(tr)
te=imp.fit(te).transform(te)
tr1=tr[:,[1,2,5,7]]
te1=te[:,[1,2,5,7]]
Y=tr[:,-1]
tr2=onehotdata[:8500]
te2=onehotdata[8500:]
print "tr1.shape",tr1.shape
print "tr2.shape",tr2.shape
train=np.column_stack((tr1,tr2))
test=np.column_stack((te1,te2))

#### kmeans ######

from sklearn.cluster import KMeans



clf = RandomForestClassifier(n_estimators=25)
clf.fit(train,Y)
pred=clf.predict(test)
li=[]
for i in range(0,len(pred)):
	li.append("Stripe "+ str(int(pred[i])))

predli=np.array(li)

d2=pd.read_csv('Initial_Test_DataOr.csv')
isin=d2.values
isin=isin[:,0]
ans=np.column_stack((isin,predli))

f=open('output28.csv','wb')
w=csv.writer(f,delimiter=',')
w.writerows(ans)
print "main prediction done"

x1,y1=train[:6800],Y[:6800]
xt,yt=train[6800:],Y[6800:]

clf.fit(x1,y1)
yy=clf.predict(xt)
print "validation prediction result", np.sum(yy==yt)*1.0/(len(yt)*1.0)



