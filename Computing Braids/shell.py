from braid import main
from webs import Braid, compose, power

#===
# Tutorial
#---
# main computes an actual braid from "Braid"
print("Heres main")
main(Braid.braid02, showinput=True)

#---
# Compose(w2, w1) allows you to compose two braids:
#
#  | F | = compose(G, F)
#  | G |  

#---
# You can compute the composition of two braids.
# Consider basis elements b1, and b2:
print("heres composition")
braid = compose(Braid.b3, compose(Braid.b3, Braid.b4))
main(braid)

#---
# For any braid that DOES NOT involve the cup/cap
# You can see the braid as it is input:
print("Here's a picture")
main(Braid.braid01, showinput = True)

#--- 
# You can take the power of an input braid
print("heres a power example")

braid = power(Braid.b3, 3)
main(braid, showinput= True)

#===
# Additional Notes
#---
# The basis Elements are Braid.b(0-5) and correspond
# to the order you have written them in notes.