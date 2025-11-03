import numpy as np 

x=[[3,2],[2,2],[3,3]]
y=[0,2,1]
x=np.array(x)
y=np.array(y)
#XTXw=XTy

x_bais=np.hstack([np.ones((x.shape[0],1)),x])
w=np.linalg.inv(x_bais.T @ x_bais)@(x_bais.T @ y)
b=w[0]
w=w[1:]
X_test = np.array([[3,2], [1,1],[0,0]])
output=b+(X_test@w)

print(np.mean((y - output)**2))

