# Code to produce pretty outputs.

import sympy as sm
from sympy import Add, Mul, Pow, Symbol, Integer, Rational
from sympy.printing.pretty.pretty import PrettyPrinter
from sympy.printing.pretty.stringpict import prettyForm

#===
# Basis Symbols
basissymbols = [
r"""| | |
| | |
| | |
""",

r"""| \ /
|  |
| / \
""",

r"""\ / |
 |  |
/ \ |
""",

r"""| \ /
|  | 
\ / \
 |  |
/ \ |
""",

r"""\ / |
 |  |
/ \ /
|  | 
| / \
""",

r"""\_|_/
 _ _
/ | \
"""
]

#=== 
# Printer
class MyPrettyPrinter(PrettyPrinter):

    basisNames = {'b0','b1','b2','b3','b4','b5'}

    #---
    # Print a beautiful equation
    def _print_Symbol(self, i):
        if i.name == "b0":
            return prettyForm(basissymbols[0])
        if i.name == "b1":
            return prettyForm(basissymbols[1])
        if i.name == "b2":
            return prettyForm(basissymbols[2])
        if i.name == "b3":
            return prettyForm(basissymbols[3])
        if i.name == "b4":
            return prettyForm(basissymbols[4])
        if i.name == "b5":
            return prettyForm(basissymbols[5])
        
        return super()._print_Symbol(i)
    
    #---
    # Return the basis element, and the coefficient in q
    def extractBasis(self, term):
        factors = Mul.make_args(term)
        basis = None
        coefficient_factors = []

        for f in factors:
            if isinstance(f, Symbol) and f.name in self.basisNames:
                basis = f
            else:
                coefficient_factors.append(f)

        if basis is None:
            return None, term
        
        coefficient = Mul(*coefficient_factors) if coefficient_factors else sm.Integer(1)

        return basis, coefficient

    #---
    # Collect terms of the coefficienticient as a polynomial in q
    def printCoefficient(self, coefficient):

        q = sm.Symbol('q')
        coefficient = sm.collect(sm.expand(coefficient), q)

        return self.printqPoly(coefficient)

    #---
    # Print Polynomial in q
    def printqPoly(self, expr):
        q = sm.Symbol('q')

        # Single number
        if expr.is_number:
            return self._print(expr)

        # Single q power: q^n
        if isinstance(expr, Pow) and expr.base == q:
            exp_pf = self._print(expr.exp)

            return prettyForm(*prettyForm('q').right(prettyForm('^'), exp_pf))

        # c * q^n
        if isinstance(expr, Mul):
            q_part    = sm.Integer(1)
            num_part  = sm.Integer(1)

            for f in Mul.make_args(expr):
                if f == q or (isinstance(f, Pow) and f.base == q):
                    q_part = q_part * f
                else:
                    num_part = num_part * f

            if q_part == 1:
                return self._print(num_part)
            
            q_pf  = self.printqPoly(q_part)

            if num_part == 1:
                return q_pf
            num_pf = self._print(num_part)

            return prettyForm(*num_pf.right(u'\N{DOT OPERATOR}', q_pf))

        # Sum: recurse on each summand
        if isinstance(expr, Add):
            terms = list(expr.as_ordered_terms())
            result = self.printqPoly(terms[0])

            for t in terms[1:]:
                t_pf = self.printqPoly(t)

                # Check sign to use + or -
                if t.could_extract_minus_sign():
                    result = prettyForm(*result.right(' - ', self.printqPoly(-t)))
                else:
                    result = prettyForm(*result.right(' + ', t_pf))

            return result

        return super()._print(expr)

    #---
    # Print a single term in the polynomial
    def printterm(self, coefficient, basis_sym):
        
        coefficient_pf = self.printCoefficient(coefficient)
        basis_pf = self._print(basis_sym)
        if coefficient == 1:
            return basis_pf
        coefficient_pf = prettyForm(*coefficient_pf.parens())
        return prettyForm(*coefficient_pf.right(u'\N{DOT OPERATOR}', basis_pf))

    #---
    # Print the addition of two terms
    def _print_Add(self, expr):
        from sympy import Add
        terms = list(expr.as_ordered_terms())

        # Separate into basis terms and non-basis terms
        basis_terms = {}   # basis_symbol -> list of coefficienticients
        other_terms = []

        for term in terms:
            basis, coefficient = self.extractBasis(term)
            if basis is not None:
                basis_terms.setdefault(basis, []).append(coefficient)
            else:
                other_terms.append(term)

        # Collect coefficienticients per basis symbol
        printed_terms = []
        for b in sorted(basis_terms, key=lambda s: s.name):
            total_coefficient = sm.Add(*basis_terms[b])
            printed_terms.append(self.printterm(total_coefficient, b))

        # Any non-basis leftovers
        for t in other_terms:
            printed_terms.append(super()._print(t))

        # Join with + / -
        result = printed_terms[0]
        for p in printed_terms[1:]:
            result = prettyForm(*result.right(' + ', p))

        return result

    #---
    # Enforce coefficient·q^n·basis order
    def _print_Mul(self, expr):
        
        basis, coefficient = self.extractBasis(expr)
        if basis is not None:
            return self.printterm(coefficient, basis)
        return super()._print_Mul(expr)
        
#---
# Print it out
def display(expression):
    print(MyPrettyPrinter().doprint(expression))

basis = [sm.Symbol('b0'), sm.Symbol('b1'), sm.Symbol('b2'), sm.Symbol('b3'), sm.Symbol('b4'), sm.Symbol('b5')]

#===
# Braid Printing
braidelement = [
r""" |   \ /
|    |
 |   / \
""",

r"""  \ /   |
   |    |
  / \   |
"""
]

def seebraid(inputbraid):
    top, bottom, web = inputbraid

    braid = r""""""
    a, b, c = top

    undrawn = web.copy()
    while undrawn:

        for section in undrawn:
            q, r, s, t = section
            if (a == s) and (b == r):
                braid += braidelement[1]
                undrawn.remove(section)
                a = t
                b = q
            
            elif (b == s) and (c == r):
                braid += braidelement[0]
                undrawn.remove(section)
                b = t
                c = q

    return display(prettyForm(braid))