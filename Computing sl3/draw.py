# Draw a knot
# Input: The PD Representation of a knot
# Output: A drawing of that knot

#===
# Imports
import matplotlib.pyplot as plt


#===
# Determine knot positivity
def positivity(pd):

    assignments = {'positive': [],
                   'negative': []}
    signedpd = []
    
    while True:
        item = pd.pop(0)
        a, b, c, d = item
        check = True

        #---
        # Determine the direction of b or d from outgoing strands in the pd
        if check:
            for next in pd:
                w, x, y, z = next

                if b == y:
                    assignments['negative'].append(item)
                    signedpd.append((item, 'negative'))
                    check = False
                    
                elif d == y:
                    assignments['positive'].append(item)
                    signedpd.append((item, 'positive'))
                    check = False
                
        #---
        # Determine the direction of b or d from already determined crossings
        if check:
            for next in assignments["positive"]:
                w, x, y, z,  = next

                if (b == w) or (b == z) or (d == x) or (d == y):
                    assignments['positive'].append(item)
                    signedpd.append((item, 'positive'))
                    check = False
                    break
                    
                elif (b == x) or (b == y) or (d == w) or (d == z):
                    assignments['negative'].append(item)
                    signedpd.append((item, 'negative'))
                    check = False
                    break

        if check:      
            for next in assignments['negative']:
                w, x, y, z = next

                if (b == w) or (b == x) or (d == y) or (d == z):
                    assignments['positive'].append(item)
                    signedpd.append((item, 'positive'))
                    check = False
                    break
                    
                elif (b == y) or (b == z) or (d == w) or (d == x):
                    assignments['negative'].append(item)
                    signedpd.append((item, 'negative'))
                    check = False
                    break

        if check:
            pd.append(item)

        if len(pd) == 0:
            break

    return signedpd

#===
def graph():

    return

#===
# Draw a knot from PD code input
def picture(signedpd):
    return

#===
# Testing
pd_3_1 = [[6, 4, 1, 3], [2, 6, 3, 5], [4, 2, 5, 1]]
pd_hopf = [[1, 2, 3, 4], [2, 1, 4, 3]]
pd_dummy = [([1, 2, 3, 4],'positive')]
pd_paper = [[5, 2, 6, 1], [4, 5, 1, 8], [12, 3, 9, 2], [3, 12, 4, 11], [9, 7, 10, 6], [7, 11, 8, 10]]
#print(positivity(pd_hopf))

picture(positivity(pd_paper))