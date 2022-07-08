import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return (x-5.1)**4
def fprime(x):
    return 4*(x-5.1)**3
x0=np.array([-10])
a=np.linspace(-10,10,1000)
plt.plot(a,func(a),'b-')
x1=[-10.]
x2=x1[:]
x3=x1[:]
x4=x1[:]
x5=x1[:]
x6=x1[:]
x7=x1[:]
x8=x1[:]
x9=x1[:]
res1=scipy.optimize.minimize(fun=func,x0=x0,method='L-BFGS-B',callback=x1.append)
res2=scipy.optimize.minimize(fun=func,x0=x0,method='BFGS',callback=x2.append)
res3=scipy.optimize.minimize(fun=func,x0=x0,method='Newton-CG',callback=x3.append,jac=fprime)
res4=scipy.optimize.minimize(fun=func,x0=x0,method='TNC',callback=x4.append)
res5=scipy.optimize.minimize(fun=func,x0=x0,method='trust-ncg',callback=x5.append,jac=fprime,hess=fprime)
res6=scipy.optimize.minimize(fun=func,x0=x0,method='trust-krylov',callback=x6.append,jac=fprime,hess=fprime)
res7=scipy.optimize.minimize(fun=func,x0=x0,method='trust-exact',callback=x7.append,jac=fprime,hess=fprime)
res8=scipy.optimize.minimize(fun=func,x0=x0,method='CG',callback=x8.append)


# print(x,min_val,info)
print('res1------------------------------------------------------')
print(res1)
print(x1)
print('res2------------------------------------------------------')
print(res2)
print(x2)
print('res3------------------------------------------------------')
print(res3)
print(x3)
print('res4------------------------------------------------------')
print(res4)
print(x4)
print('res5------------------------------------------------------')
print(res5)
print(x5)
print('res6------------------------------------------------------')
print(res6)
print(x6)
print('res7------------------------------------------------------')
print(res7)
print(x7)
print('res8------------------------------------------------------')
print(res8)
print(x8)
plt.plot(x1,[func(i)  for i in x1],'o-')
plt.plot(x2,[func(i)  for i in x2],'o-')

plt.show()