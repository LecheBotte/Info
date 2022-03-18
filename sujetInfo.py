from numpy import min, max, zeros, roots, real
from scipy import linspace
from scipy.signal import lti, step
from matplotlib import pyplot as plt
from random import random

d0 = 1
d1 = 1.13
d2 = 0.273
d3 = 0.0072
K = 8

numG = [K]
denG = [d3,d2,d1,d0]

G = lti(numG, denG)