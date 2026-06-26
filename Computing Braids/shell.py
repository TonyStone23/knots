from braid import main
from webs import Braid, compose, power

#===
# Tutorial
#---
# main computes an actual braid from "Braid"
print("\n\n--- Heres main ---")
main(Braid.braid02, showinput=True)

#---
# Compose(w2, w1) allows you to compose two braids:
#
#  | F | = compose(G, F)
#  | G |  

#---
# You can compute the composition of two braids.
# Consider basis elements b1, and b2:
print("\n\n--- Heres braid composition ---")
braid = compose(Braid.b3, compose(Braid.b3, Braid.b4))
main(braid)

#---
# For any braid that DOES NOT involve the cup/cap
# You can see the braid as it is input:
print("\n\n--- Here's a picture ---")
main(Braid.braid01, showinput = True)

#--- 
# You can take the power of an input braid
print("\n\n--- heres a power example ---")
braid = power(Braid.b5, 3)
main(braid)

#===
# Additional Notes
#---
# The basis Elements are Braid.b(0-5) and correspond
# to the order you have written them in notes.

#---
# You can build braids as a composition of basis elements, and take their power.
print("\n\n--- Building a braid to take its power ---")
newBraid = compose(Braid.b2, Braid.b3)
cubedBraid = power(newBraid, 3)
main(cubedBraid)