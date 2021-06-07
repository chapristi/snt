import pandas as pa 
import numpy as np 
from collections import defaultdict

dc = defaultdict(list)
counter = 1
while counter <= 20 :
  inp = input("ENTRER UN PRENOM : ")
  inpx = "inp"  + str(counter)
  dc[inpx]  = inp
  counter += 1 
  
liste = sorted(dc.values(),reverse=False) 
listeinv = sorted(dc.values(),reverse=True)

res = {
  "noms" : liste 
}
df1 = pa.DataFrame(data = res)
df1.to_csv(r'prenom.csv',sep = ',',index = None)

np.random.seed(2)
df2 = pa.DataFrame({
  'nom1' : np.random.choice(a = liste, size = 20 ),
  'nom2' :  np.random.choice(a = listeinv,size = 20)
  })
 
df2.to_csv(r'reseau.csv',sep = ',',index = None)
