#===
# Imports
import pandas as pd
import sympy as sm
from statesum import sl3
from data import collect, prepare
from trials import trials

#===
# Evaluate the algorithm
def evaluate(computedfile, truthfile):

    names = list(pd.read_csv(computedfile)['Name'])
    computed = list(pd.read_csv(computedfile)['sl3'])
    truth = list(pd.read_csv(truthfile)['HOMFLY'])
    errors = []
    correct = []

    items = len(computed)
    count = 0
    for i in range(items):
        if sm.sympify(computed[i]) == sm.sympify(truth[i]):
            correct.append(names[i])
            count += 1
        else:
            errors.append(names[i])
        print(f"{(count/items)*100:.5}% correct")
    
    print("correct: \n", correct)
    print("errors: \n", errors)

#===
# Main Method
def main(knotdata, outputfile, truthfile):
    names, pds, homflys, items = collect(knotdata)
    
    output = pd.DataFrame(columns = ('Name', 'sl3'))

    for i in range(items):
        print(f"{(i/items)*100:.3}% complete")
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
inputknots, outputsl3s, truthfile = trials[1]

main(inputfolder+inputknots, outputfolder+outputsl3s, inputfolder+truthfile)
