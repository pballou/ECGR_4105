'''
h = theta_1*X_1+theta_0
J = 1/(2*m)*[sum(i=1 to m) (Y-h)^2], J is loss
1<i<m(datapoints)
0,j,n(dimensionality)

theta_new = theta_old - alpha*(d_J/d_theta) where d_J/d_theta = d_J/d_theta_J = 1/m * [sum(i=1 to m) (Y-h)*X_j

h(x):
use h = theta_1*x_1 + theta_0*x_0 where x_0 = [1 1 1 ... 1]
concatenate x_0 matrix to x_1 to simplify multiplication (x is the whole input matrix with size [m,n])
theta matrix is (n,1)
now we can say h(x) = x.*theta -> result is matrix with size [m,1]


J:
for i=1 to m
    J = (Y'-h')^2
J = J/2m


d_J/d_theta_j:
subtract h-Y and put in temp array of size [m,1], we subtract all pairs until temp matrix is full
x is [m,n] matrix
use transpose(x) and multiply by temp array of size [m,1]
so, [n,m] * [m,1] = [n,1] which is our d_J/d_theta array

finally:
theta_new = theta_old - alpha*((d_J/d_theta)/m)

once you see results, use initial values closer to found theta and it will converge faster
alpha<=.01
'''