from braid import main
from webs import Braid, compose, power, build
from printing import seebraid

#===
# Go crazy
#main(Braid.garside)
print(main(power(Braid.garside, 2), False))
print(main(power(Braid.garside, 1), False))