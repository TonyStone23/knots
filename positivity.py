#===
# Determine the posititivty of a knot diagram 
def positivity(pd):
    assignments = {'positive': [],
                   'negative': []}
    
    signedpd = []

    item = pd.pop(0)
    assignments['positive'].append(item)
    signedpd.append((item, 'positive'))
    
    while True:

        item = pd.pop(0)
        a, b, c, d = item

        check = True

        if check:
            for prior in assignments["positive"]:
                w, x, y, z, = prior

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
            for prior in assignments['negative']:
                w, x, y, z = prior

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
# Testing
pd_11a_266 = [[6,2,7,1],[10,3,11,4],[14,7,15,8],[18,11,19,12],[12,6,13,5],[4,18,5,17],[20,16,21,15],[16,10,17,9],[22,13,1,14],[2,19,3,20],[8,21,9,22]]

for entry in positivity(pd_11a_266):
    crossing, sign = entry
    print(sign, crossing)