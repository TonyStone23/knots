from braid import main
from webs import Braid, compose, power, build
from printing import seebraid

#===
# Go crazy
print("Garside^1:")
main(power(Braid.garside, 1), False)
print("Garside^2:")
main(power(Braid.garside, 2), False)