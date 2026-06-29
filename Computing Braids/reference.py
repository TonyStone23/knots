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
#  | F | = compose(G, F)
#  | G |  

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

#---
# For any braid that DOES NOT involve the cup/cap
# You can see the braid as it is input:
print("\n\n--- Here's a picture ---")
main(Braid.braid01, showinput = True)
# You could also just seebraid it
print("\n\n--- Same picutre, but just the drawing ---")

seebraid(Braid.braid01)

#--- 
# You can take the power of an input braid
print("\n\n--- Here's a power example ---")
braid = power(Braid.b5, 3)
main(braid)

#---
# You can build braids as a composition of basis elements, and take their power.
print("\n\n--- Building a braid to take its power ---")
newBraid = compose(Braid.b2, Braid.b3)
cubedBraid = power(newBraid, 3)
main(cubedBraid, showinput=True)

#---
# You can build a braid from a list of basis components:
print("\n\n--- Building a braid ---")
elements = [Braid.b3, Braid.b4, Braid.b1, Braid.b4, Braid.b2]
braid = build(elements)
main(braid, showinput=True)