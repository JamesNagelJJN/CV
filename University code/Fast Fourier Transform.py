import numpy as np
import matplotlib.pyplot as plt
from operator import add

f = [-0.2, -0.1, 0.3, 0.2, 0.4, 0.5, 0, -0.4, -0.4, -0.2, 0.1, 0.2, 0.2, 0.1, 0.1, -0.1]

fft = np.fft.fft(f)
# fft applies the fast fourier transform to the data
n = len(f)
a = []
b = []
for i in range(0, n):
    a.append(fft[i].real / n)
    b.append(fft[i].imag / n)
    # a and b are the coefficients of the fourier series

d = []
g = []
x = np.linspace(0, 15/8*np.pi, n)
for j in range(n):
    for i in range(n):
        d.append(a[j]*np.cos(j * x[i]))
        g.append(b[j]*np.sin(j * x[i]))
        # These two for loops add the cos and sin (with a and b coefficients) terms to two different lists
h = 16
s = 0
j = []
o = []
w = []
for i in range(n):
    j.append(g[s:h])
    o.append(d[s:h])
    h += 16
    s += 16
    # This for loop adds each individual sine and cosine wave to lists j and o

for i in range(n):
    w.append(list(map(add, j[i], o[i])))
    # Each value in the list w is a combination of the sine and cosine waves

for i in range(1,n):
    plt.plot(w[i])
    plt.title("Individual Fourier series lines")
    plt.draw()
    plt.pause(0.5)
    plt.xlabel("Data points")
    plt.ylabel("Amplitude")
plt.show(block=True)
# This graph shows each line that makes up the fourier series (each line is a combination of the sine and cosine waves)
# Some of the lines on the graph over lap!


plt.ion()
# plt.ion allows for graphs to become animated/refresh
t = []

for i in range(n):
    u = []
    for p in range(1, n):
        u.append(w[-p][-i])
        # The list u adds each pth value of each ith list together
    t.append(1/2*a[0]+sum(u))
    # The list t holds the combined values for the pth item of all the ith lists
    plt.pause(0.02)
    plt.xlabel("Data points")
    plt.ylabel("Amplitude")
    plt.clf()
    plt.plot(t)
    plt.draw()
    # plots each point on a graph
plt.plot(f)
plt.legend(["Truncated fourier series","Original plot"])
plt.title("Truncated fourier series plotted with the original data")
plt.show(block=True)
