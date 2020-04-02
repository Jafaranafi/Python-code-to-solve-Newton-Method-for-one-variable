import numpy as np
import matplotlib.pyplot as plt
def f(x):
	return x-1/(2**x)
def g(x):
	return 1+np.log(2)*1/(2**x)
n=18
#x=2
u=np.zeros(19)
u[0]=0

for i in range(n):
	u[i+1]=u[i]-f(u[i])/g(u[i])
print (u)
t=np.linspace(0,10, 19)
plt.xlabel("x")
plt.ylabel("y")
plt.title("$x-1/(2**x)$")
plt.plot(t,u,'r.-')
plt.show()



