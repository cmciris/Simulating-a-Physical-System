#!/usr/bin/env python

from math import sqrt
import random
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pylab

class Gas():
    " a simulation experiment for ideal gas "

    def __init__(
            self,
            N,  # the amount of molecules
            totalEnergy,  # the total energy for the experiment
            steps,  # the number of loops
            state=0,  # init state
            visuals=True  # if visuals
    ):
        # initializing
        self.N = N
        self.totalEnergy = float(totalEnergy)
        self.steps = steps
        self.state = state


    def setState(self, N, state):
        if state:
            self.molecules = [sqrt(2 * self.totalEnergy / N)] * N
            self.demon = 0.
        else:
            self.molecules = [0.] * N
            self.demon = float(self.totalEnergy)

        self.Dv = sqrt(2 * self.totalEnergy / N / 10)
        self.demonEnergy = [self.demon]
        self.systemlist = [ self.totalEnergy - self.demon ]

    def trial(self, n):
        # choose a random molecule
        k = random.randint(0, n - 1)
        # Generate a random number
        deltaV = random.uniform(-self.Dv, self.Dv)
        # calculate the change in energy
        vOld = self.molecules[k]
        vNew = vOld + deltaV
        deltaEnergy = (vNew ** 2 - vOld ** 2) / 2
        # If the change in energy is valid
        if self.demon >= deltaEnergy:
            self.molecules[k] = vNew
            self.demon -= deltaEnergy
        else:
            pass

    def loop(self, n):
        for _ in range(n):
            self.trial(n)
        self.demonEnergy.append(self.demon)
        self.systemlist.append(self.totalEnergy - self.demon)

    def simutulation(self, n):
        for _ in range(self.steps):
            self.loop(n)
        self.systemEnergy = 0
        for x in self.systemlist:
            self.systemEnergy += x
        self.systemEnergy = self.systemEnergy / self.steps

    def N_versus_Energy(self):
        x = range(50, self.N + 1, 50)
        y2 = []
        for i in x:
            self.setState(i, self.state)
            self.simutulation(i)
            y2.append( self.systemEnergy )
        y1 = [ self.totalEnergy ] * len(x)
        plt.grid(True)
        l1, = plt.plot(x, y1, "ro-")
        l2, = plt.plot(x, y2, "bo-")
        plt.title("N vs. Energy")
        plt.xlabel("N")
        plt.ylabel("Energy")
        plt.legend((l1, l2), ("Total Energy", "System Energy"), loc="upper right", shadow=True)

    def Final_Molecule_Velocity(self):
        plt.grid(True)
        plt.hist(self.molecules, color='c')
        plt.xlabel("V")
        plt.ylabel("Frequency")
        plt.title("Final particle velocity distribution")

    def Demon_Energy(self):
        plt.grid(True)
        plt.hist(self.demonEnergy, color='m')
        plt.xlabel("Demon Energy")
        plt.ylabel("Frequency")
        plt.title("Demon Energy Histogram")

    def Demon_Energy_Time(self, k=0):
        """
            demon energy time
        """
        symbol = ['*', 'k', 'ro']
        pylab.grid(True)
        xs = []
        ys = []
        pylab.ion()
        for i in range(len(self.demonEnergy)):
            xs.append(i)
            ys.append(self.demonEnergy[i])
        pylab.plot(xs,ys,symbol[k])


    def show1(self):
        plt.figure(figsize=(15,5))
        plt.subplot(1, 2, 1)
        self.N_versus_Energy()

        plt.subplot(1, 2, 2)
        self.Final_Molecule_Velocity()

        plt.show()


    def show2(self):
        plt.figure(figsize=(15,5))
        plt.subplot(1, 2, 1)
        self.N_versus_Energy()

        plt.subplot(1, 2, 2)
        self.Demon_Energy()

        plt.show()

    def show3(self, k=0):
        plt.figure(figsize=(15,5))
        plt.subplot(1, 2, 1)
        self.N_versus_Energy()

        plt.subplot(1, 2, 2)
        self.Demon_Energy_Time(k)

        plt.show()

    def showAll(self, k=0):
        plt.figure(figsize=(16,8))
        plt.subplot(2, 2, 1)
        self.N_versus_Energy()

        plt.subplot(2, 2, 2)
        self.Final_Molecule_Velocity()

        plt.subplot(2, 2, 3)
        self.Demon_Energy()

        plt.subplot(2, 2, 4)
        self.Demon_Energy_Time(k)

        plt.show()
