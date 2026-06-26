from braid import main
from webs import Braid, compose

#===
# Tutorial
#---
# main computes an actual braid from "Braid"
print("Heres main")
main(Braid.braid02)

#---
# Compose(w2, w1) allows you to compose two braids:
#
#  | F | = compose(G, F)
#  | G |  

#---
# You can compute the composition of two braids.
# Consider basis elements b1, and b2:
print("heres composition")
braid = compose(Braid.b1, Braid.b2)
main(braid)

#---
# For any braid that DOES NOT involve the cup/cap
# You can see the braid as it is input:
print("Here's a picture")
main(Braid.braid01, showinput = True)

#===
# Additional Notes
#---
# The basis Elements are Braid.b(0-5) and correspond
# to the order you have written them in notes.