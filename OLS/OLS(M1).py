import numpy as np

x=[[1,2],[2,2],[3,3]]
y=[0,2,1]
x=np.array(x)
y=np.array(y)
value_x=x[:,0]
value_y=y
mean_x=value_x.mean()
mean_y=value_y.mean()

num=np.sum((value_x-mean_x)*(value_y-mean_y))
den=np.sum((value_x-mean_x)**2)

w=num/den


b=mean_y-(w*mean_x)

print(w)



    



