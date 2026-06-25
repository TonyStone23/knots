# Defining the basis, and basis multiplication
# This is an implementation of the multiplication table, See Computing Braids/ for braid computations

#===
# Imports
import sympy as sm

#=== 
# Quantum Terms
q = sm.var('q')
quantum2 = sm.var('[2]')
quantum3 = sm.var('[3]')

#=== 
# Basis Class
class BasisElement(sm.Symbol):
    is_commutative = False

    def __mul__(self, other):
        if isinstance(other, BasisElement):
            return webMultiplication(self, other)
        return super().__mul__(other)
    
#---
# Basis elements
#~~~
# Basis elements
b0 = BasisElement('b0')
b1 = BasisElement('b1')
b2 = BasisElement('b2')
b3 = BasisElement('b3')
b4 = BasisElement('b4')
b5 = BasisElement('b5')

#~~~
# Basis
basis = [b0, b1, b2, b3, b4, b5]

#---
# Multiplication Table
B = [
    [b0, b1, b2, b3, b4, b5],
    [b1, quantum2 * b1, b4, b1 + b5, quantum2 * b4, quantum2 * b5],
    [b2, b3, quantum2 * b2, quantum2 * b3, b2 + b5, quantum2 * b5 ],
    [b3, quantum2 * b3, b2 + b5, b3 + quantum2 * b5, b2 + b5, quantum2**2 * b5],
    [b4, b1 + b5, quantum2 * b4, b1 + b5, b4 + quantum2 * b5, quantum2**2 * b5],
    [b5, quantum2 * b5, quantum2 * b5, quantum2**2 * b5, quantum2**2 * b5, quantum2 * quantum3 * b5]
    ]

#---
# Web Multiplication
def webMultiplication(bi, bj):
    i = int(bi.name[1:])
    j = int(bj.name[1:])
    return B[i][j]

print(b1 * b4)