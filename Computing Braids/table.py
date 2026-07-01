#===
# Compute multiplication table for basis elements
from braid import evaluate
from webs import Braid, compose

basis = [Braid.b0, Braid.b1, Braid.b2, Braid.b3, Braid.b4, Braid.b5]

table = []
for i in range(6):
    row = []
    for j in range(6):
        top, bottom, web = compose(basis[j], basis[i])
        row.append(evaluate(top, bottom, web))
    table.append(row)

for row in table:
    print(row)

#===
# Output:
# 
# [b0, b1, b2, b3, b4, b5]
# [b1, [2]*b1, b3, [2]*b3, b1 + b5, [2]*b5]
# [b2, b4, [2]*b2, b2 + b5, [2]*b4, [2]*b5]
# [b3, b1 + b5, [2]*b3, [2]*b5 + b3, [2]*(b1 + b5), [2]**2*b5]
# [b4, [2]*b4, b2 + b5, [2]*(b2 + b5), [2]*b5 + b4, [2]**2*b5]
# [b5, [2]*b5, [2]*b5, [2]**2*b5, [2]**2*b5, [2]*[3]*b5]

