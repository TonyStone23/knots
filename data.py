#===
# Imports
import sympy as sm
import random as r
import pandas as pd

#===
# Global variables
q = sm.symbols('q')
v = sm.symbols('v')
z = sm.symbols('z')
quantum3 = (q**2 + 1 + q**(-2))

#===
# Get raw data
def collect(inputfile):
    knots = pd.read_csv(inputfile)
    names = list(knots['Name'])
    pds = list(knots['PD'])
    homflys = list(knots['HOMFLY'])
    items = len(names)
    return names, pds, homflys, items

#===
# Prepare a PD code for computation
def prepare(pd):
    pd = pd.strip("[]").split("];[")
    pd = [list(map(int, i.strip("[]").split(";"))) for i in pd]
    return pd

def write(pd):
    pd  = "[" + ";".join("[" + ";".join(map(str, i)) + "]" for i in pd) + "]"
    return pd

#===
# Get ground truth for sl3
def convert(homfly):

    homfly = sm.sympify(homfly)
    sl = homfly.subs({
        v: q**-3, 
        z: q - q**(-1) 
        })
    sl = sl * quantum3
    sl = sm.simplify(sl)
    sl = sm.expand(sl)
    
    return sm.powdenest(sl, force = True)

#===
# Apply an R1 move
def R1(pd):
    max = len(pd) * 2

    item = pd.pop(r.randint(0, len(pd) - 1))
    a, b, c, d = item

    if a == b:
        pd.append([max + 1, b, c, d])
        pd.append([b, max + 1, max + 2, max + 2])

        return pd

    for next in pd:
        w, x, y, z = next

        if y == d:
            pd.append([a, b, c, max + 1])
            pd.append([max + 2, max + 2, max + 1, y])
            break
    
    return pd

#===
# Apply many R1 moves
def mangle(pd, moves):
    for m in range(moves):
        pd = R1(pd)
    return pd

#===
# Build dataset of knots
def main(moves, inputfile, outputfile, outputtruth):
    columns = ('Name', 'PD')
    truthcolumns = ('Name', 'HOMFLY')
    names, pds, homflys, items = collect(inputfile)
    
    output = pd.DataFrame(columns = columns)
    truths = pd.DataFrame(columns = truthcolumns)

    for i in range(items):
        print(f"{i/items:.3f}% complete")
        subframe = pd.DataFrame(columns = columns)
        subtruth = pd.DataFrame(columns = truthcolumns)

        if moves > 0:
            for m in range(moves):
                new = write(mangle(prepare(pds[i]), m))
                subframe.loc[m] = [names[i],new]

                truth = convert(homflys[i])
                subtruth.loc[m] = [names[i], truth]
                
        else:
            new = write(mangle(prepare(pds[i]), m))
            subframe.loc[0] = [names[i],new]

            truth = write(convert(homflys[i]))
            subtruth.loc[0] = [names[i], truth]

        output = pd.concat([output, subframe])
        truths = pd.concat([truths, subtruth])

    print("Complete")
    output.to_csv(outputfile, index = False)
    truths.to_csv(outputtruth, index = False)

if __name__ == "__main__":
    #===
    # Input Folders
    inputfolder = 'input/'
    inputfile = 'knotsample.csv'
    outputfile = 'knotsampleinput.csv'

    #---
    # Ground Truth
    outputtruth = 'knotsampletruth.csv'

    main(1, inputfolder+inputfile, inputfolder+outputfile, inputfolder+outputtruth)