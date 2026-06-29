from braid import main
from webs import Braid, compose, power, build
from printing import seebraid

#===
# Convention and Function Notes
#---
# The basis Elements are Braid.b(0-5) and correspond
# to the order you have written them in notes.
#---
# The class "Braid" is really meant to be a sort of 'container',
# This is not an object-oriented implementation.

#---
# compose(w2, w1) allows you to compose two braids:
#
#  | G |  
#  | F | = compose(G, F)

#---
# power(braid, n) allows you to take the power of a braid

#---
# build([braid1, braid2, ..., braidn]) allows you to build a braid:
#
# compose(braid1, (compose (braid2, compose(..., braidn))))

#===
# Tutorial
#---
# main computes an actual braid from "Braid"
print("\n\n--- Here's main ---")
main(Braid.braid02, showinput=True)

#---
# You can compute the composition of two braids.
# Consider basis elements b1, and b2:
print("\n\n--- Here's braid composition ---")
braid = compose(Braid.b3, compose(Braid.b3, Braid.b4))
main(braid)