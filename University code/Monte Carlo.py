import numpy as np
import random
import matplotlib.pyplot as plt
import math

it = int(input("\n Please give the number of points you would like the Monte Carlo integration method to trial for each dimension (higher the number of points the more accurate the simulation) : "))
r = 1
# input for radius
n = 16
f = range(2, n)
# range for graph plotting
p = []
for i in range(n):
    p.append((np.pi ** (i / 2) / math.gamma((i / 2) + 1))*r**i)
    # This for loop calculates the actual values of the volume of a sphere up to the 15 dimension with radius 1


class Sphere:
    N = 0
    # N is the total number of points cast
    count = 0
    # count is a counter for each time a cast point is within the volume of the sphere

    def __init__(self, j):
        n = 16
        # This function sets up the cast point (aka radius)
        k = []
        for i in range(n):
            self.x = random.uniform(-r, r)
            k.append(self.x)
            # This for loop gets the individual values in each dimension in a list
        b = np.array(k)
        # convert list to an array
        n = np.square(b)
        # square each value within the array
        self.radius = np.sqrt(sum(n[0:j]))
        # the radius takes the root of the sum of the array up to the given dimension j

    def sphere(self):
        global count
        global N
        # making count and N global so i can change their values in this function
        if self.radius <= r:
            count += 1
            N += 1
            # this if statement works out if the cast point is within the sphere, if so +1 to count and total N
        else:
            N += 1
            # if the cast point is not enclosed within the sphere count will stay the same but N still increases by 1
        return count


g = []
for j in range(n):
    # n is the number of dimensions
    X = Sphere(j)
    N = 0
    count = 0
    # need to reset N and count for each new dimension
    for i in range(it):
        X.__init__(j)
        X.sphere()
        # X.__init__(j) runs with respect to j (each dimension)
        # X.sphere() needs to be run to calculate the count and N values
    g.append(count/N*((2*r)**j))
    # this list calculates the volume of the sphere in each corresponding dimension (j value)

y = np.array(p)
print("\n","     This list is the values for the Gamma function n-ball volumes :",np.round(y[2:n], 2), "\n","This list is the values for the Monte Carlo method n-ball volumes :" ,np.round(g[2:16], 2))

plt.scatter(f, g[2:n], color='purple')
plt.scatter(f, p[2:n], color='cyan')
plt.xlabel("Dimensions")
plt.ylabel("'Volume' of the sphere")
plt.legend(["Monte Carlo", "Gamma function"])
plt.xticks(f)
plt.yticks(range(int(max(p)+2)))
plt.show()
# this code plots the graph from dimensions 2-15 with both the monte carlo calculation and gamma function
