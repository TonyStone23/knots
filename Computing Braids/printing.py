import sympy as sm
from sympy.printing.pretty.pretty import PrettyPrinter
from sympy.printing.pretty.stringpict import prettyForm

# Your ASCII art — make it whatever you like!
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

r"""\ / |
 |  |
/ \ /
|  | 
| / \
""",

r"""| \ /
|  | 
\ / \
 |  |
/ \ |
""",

r"""\_|_/
 _ _
/ | \
"""
]

class MyPrettyPrinter(PrettyPrinter):
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
        
def display(expr):
    print(MyPrettyPrinter().doprint(expr))

basis = [sm.Symbol('b0'), sm.Symbol('b1'), sm.Symbol('b2'), sm.Symbol('b3'), sm.Symbol('b4'), sm.Symbol('b5')]

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

def seebraid(top, bottom, web):

    braid = r""""""
    a, b, c = top

    undrawn = web.copy()
    while undrawn:

        for section in undrawn:
            q, r, s, t = section
            if (a == s) and (b == r):
                braid += braidelement[0]
                undrawn.remove(section)
                a = t
                b = q
            
            elif (b == s) and (c == r):
                braid += braidelement[1]
                undrawn.remove(section)
                b = t
                c = q

    return display(prettyForm(braid))