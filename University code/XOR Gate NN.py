import random
import numpy as np
import time

print("\n","Hello, this code trains a neural network to match an XOR logic gate via the metropolis algorithm.", "\n"
      "    ","This code can solve almost instantly or can take a few minutes so please be patient.", "\n",
      "   "*6,"If it is taking too long just re-run the code", "\n")
start_time = time.time()
tt = [[0, 0, 0, 0],
      [0, 0, 1, 1],
      [0, 1, 0, 1],
      [0, 1, 1, 0],
      [1, 0, 0, 1],
      [1, 0, 1, 0],
      [1, 1, 0, 0],
      [1, 1, 1, 1]]


finaloutput = []
# finaloutput is a list that holds the current values for the outputs and when completed holds the finaloutput's
Weights = []
# Weights the same as finaloutput but for weights
Weight = []
# Weight is the list that holds the values for each weight
sig = 1.4
# sig is short for sigma which is used when a random change is made to the weights this multiplied by a random value gives the change

for i in range(16):
    Weight.append(random.uniform(-1, 1))
    # This for loop is for assigning each Weight a random value


class XOR:
    @staticmethod
    # used @staticmethod so code knows it is static
    def act(x):
        return 1.0 / (1 + np.exp(-x))
    # This is the activation function used to calculate the value of each node

    def nodes(self, e):
        input1 = tt[e][0]
        input2 = tt[e][1]
        input3 = tt[e][2]
        hidden4 = self.act(Weight[0] + Weight[4] * input1 + Weight[7] * input2 + Weight[10] * input3)
        hidden5 = self.act(Weight[1] + Weight[5] * input1 + Weight[8] * input2 + Weight[11] * input3)
        hidden6 = self.act(Weight[2] + Weight[6] * input1 + Weight[9] * input2 + Weight[12] * input3)
        output7 = self.act(Weight[3] + Weight[13] * hidden4 + Weight[14] * hidden5 + Weight[15] * hidden6)
        return output7
    # This is the nodes function that when called with a given e value will give the output of the neural network

    def initialenergy(self):
        errorlist = []
        for e in range(len(tt)):
            error = abs((self.nodes(e) - tt[e][3])) ** 2
            errorlist.append(error)
        energy0 = sum(errorlist) / 7
        return energy0
    # This function is called initialenergy which calculates the initial energy value of the neural network

    def energy(self):
        energy0 = self.initialenergy()
        # energy 0 is the initial energy of the neural network
        accept = 0
        # variable for when the energy difference is less than 0
        deny = 0
        # variable for when the energy difference is more than 0 and p is more than the compare variable
        beta = 1000
        # beta is a variable that is used in the compare variable, beta is changed based on whether the algorithm requires 'heating' or 'cooling'
        h = 0.1
        # h is a constant which is used for a random value generator
        y = []
        # y is a list that stores the current output values
        errorlist = []
        randomlist = []
        for t in range(16):
            errorlist = []
            randomvalue = random.uniform(-h, h)
            randomlist.append(randomvalue)
            Weight[t] = Weight[t] + randomvalue * sig
        for j in range(len(tt)):
            y.append(self.nodes(j))
            error = abs((y[j] - tt[j][3])) ** 2
            errorlist.append(error)
        # The number 7 is from the number of output nodes * the number of patterns
        energy1 = sum(errorlist) / 7
        # The energy is the change in energy between Energy1 and Energy0
        energy = energy1 - energy0
        # compare is a calculated value to be compared to p a random value
        compare = np.exp(-beta * energy)
        p = random.uniform(0, 1)
        # The following if elif and else statements update the energy to the
        # new energy depending on their values
        if energy < 0:
            energy0 = energy1
            accept += 1
            beta += 100
        elif p < compare:
            energy0 = energy1
            accept += 1
            beta += 100
        else:
            energy0 = energy0
            deny += 1
            beta -= 100
            for h in range(16):
                # Here the changes in the weights are reversed if the new energy is greater
                # than the previous
                Weight[h] = Weight[h] - randomlist[h] * sig
        # The list Weights
        Weights.append(Weight)
        finaloutput.append(y)
        return accept, deny, energy0
    # This big function is called energy and will work out the new energy of the neural network and implement the metropolis algorithm


xx = []
c = XOR()
#assign c to the class so i am able to call it with a given function
while True:
    # This while True loop is so the program will continuously run until a solution is found
    r = 0
    # r is a running total for each new finaloutput to see if all of the finaloutputs are correct
    xx.append(c.energy())
    # xx is a list used later to calculate the acceptance rate
    for i in range(len(tt)):
        # this for loop is to see if the output of the neural network matches the corresponding values in the tt
        if int(round(finaloutput[-1][i])) == tt[i][3]:
            r += 1
    if r == 8:
        # breaks the while True loop if outputs match on all 8 layers of tt
        break

# all code below this point is purely for display output

print(" "*13 + "output" + " "*5 + "truth")

for i in range(8):
    if int(round(finaloutput[-1][i])) == tt[i][3]:
        print("correct", int(round(finaloutput[-1][i])), tt[i][3], sep=' ' * 9)
    else:
        print("wrong", int(round(finaloutput[-1][i])), tt[i][3])

print("\n", "The following values are the weights associated with the given node", "\n")

print(" i", round(Weight[0], 3), "    ", round(Weight[1], 3), "    ", round(Weight[2], 3),
      "    ", round(Weight[3], 3), "\n",
      "h4", round(Weight[4], 3), "     ", round(Weight[7], 3), "    ", round(Weight[10], 3), "\n",
      "h5", round(Weight[5], 3), "    ", round(Weight[8], 3), "    ", round(Weight[11], 3), "\n",
      "h6", round(Weight[6], 3), "    ", round(Weight[9], 3), "    ", round(Weight[12], 3), "\n",
      "o7", round(Weight[13], 3), "    ", round(Weight[14], 3), "    ", round(Weight[15], 3), "\n")

accept1 = sum(xx[0] for xx in xx)
deny1 = sum(xx[1] for xx in xx)

print("The acceptance rate is :", round(accept1/(deny1+accept1), 3), "\n",
      "Number accepted :", accept1, "\n", "Number denied :", deny1)

print("\n", "The time taken to run this code is : ", round(time.time() - start_time, 3), "seconds")