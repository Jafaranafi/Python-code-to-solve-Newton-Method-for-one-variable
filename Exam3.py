import numpy as np
#Example 3 of Newton method
import matplotlib.pyplot as plt
def f(x):
	return np.exp(x)-x**2+3*x-2
def g(x):
	return np.exp(x)-2*x+3
n=18
u=np.zeros(19)
u[0]=0
for i in range(n):
	u[i+1]=u[i]-f(u[i])/g(u[i])
print (u)
t=np.linspace(0,10, 19)
plt.xlabel("x")
plt.ylabel("y")
plt.title("$np.exp(x)-x**2+3*x-2$")
plt.plot(t,u,'r.-')
plt.show()


