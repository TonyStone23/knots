import sympy as sm
import random as r
import pandas as pd
from trials import trials

#===
# Global variables
q = sm.symbols('q')
v = sm.symbols('v')
z = sm.symbols('z')

target = q**18 - 3*q**16 + 3*q**12 - 5*q**10 + 7*q**8 - q**6 + 4*q**2 - 7 + 6/q**2 - 6/q**4 + 2/q**6 + 4/q**8 - 4/q**10 + 3/q**12 - 1/q**14
output = q**18 - 3*q**16 + 3*q**12 - 5*q**10 + 7*q**8 - q**6 + 4*q**2 - 7 + 6/q**2 - 6/q**4 + 2/q**6 + 4/q**8 - 4/q**10 + 3/q**12 - 1/q**14

print(sm.simplify(output - target))