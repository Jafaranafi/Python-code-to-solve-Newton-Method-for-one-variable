import numpy as np
#This example is for example 1 of Newton method for one variable
import matplotlib.pyplot as plt
def f(x):
	return x**2-1
def g(x):
	return 2*x
n=18
u=np.zeros(19)

u[0]=2
for i in range(n):
	u[i+1]=u[i]-f(u[i])/g(u[i])
print (u)
t=np.linspace(2,10, 19)
plt.xlabel("x")
plt.ylabel("y")
plt.title("$x**2-1$")
plt.plot(t,u,'r.-')
plt.show()


