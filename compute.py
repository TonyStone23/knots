#===
# Imports
import pandas as pd
import sympy as sm
from statesum import sl3
from workdata import collect, prepare

#===
# Evaluate the algorithm
def evaluate(computedfile, truthfile):

    computed = list(pd.read_csv(computedfile)['sl3'])
    truth = list(pd.read_csv(truthfile)['HOMFLY'])

    items = len(computed)
    count = 0
    for i in range(items):
        if sm.sympify(computed[i]) == sm.sympify(truth[i]):
            count += 1
        print(f"{(count/items)*100:.5}% correct")

#===
# Main Method
def main(knotdata, outputfile, truthfile):
    names, pds, homflys, items = collect(knotdata)
    
    output = pd.DataFrame(columns = ('Name', 'sl3'))

    for i in range(items):
        print(f"{i/items:.3}% complete")
        print(f"computing: {names[i]}")
        
        computedsl3 = sl3(prepare(pds[i]))
        output.loc[i] = [names[i], computedsl3]

    print("Complete")
    output.to_csv(outputfile, index=False)

    evaluate(outputfile, truthfile)

#===
# Path variables
#---
# Input/Output folders
inputfolder = 'input/'
outputfolder = 'output/'

#---
# Computed sl3s
inputknots = 'knotsample.csv'
outputsl3s = 'knotoutputsample.csv'
truthfile = 'knotsampletruth.csv'

main(inputfolder+inputknots, outputfolder+outputsl3s, inputfolder+truthfile)