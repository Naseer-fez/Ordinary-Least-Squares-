import numpy as np 

x = np.array([[3,2],
              [2,2],
              [3,3]])
y = np.array([0,2,1])

x_bais=np.hstack([(np.ones((x.shape[0], 1))), x])

w=np.zeros(x_bais.shape[1])

lr=0.01
epoooch=1000

for i in range(epoooch):
    x_predict=x_bais@w
    gradient=-2*x_bais.T@(y-x_predict)
    w=w-(gradient*lr)
    w=np.maximum(w,0)
    
print(w)
