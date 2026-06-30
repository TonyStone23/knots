from braid import sl3
from webs import Braid, compose, power, build
from printing import seebraid

#===
# Go crazy
print("Garside^1:")
sl3(power(Braid.garside, 1))

print("Garside^2:")
sl3(power(Braid.garside, 2))