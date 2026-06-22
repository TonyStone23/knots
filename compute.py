# Computation for large amoutns of knots

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
# Path variables
#---
# Input/Output folders
inputfolder = 'input/'
outputfolder = 'output/'

#---
# Computed sl3s
inputknots, outputsl3s, truthfile = trials[0]

#===
# Main Method
def main(knotdata, outputfile, truthfile):
    names, pds, homflys, items = collect(knotdata)

    # Determine which knots have already been computed
    try:
        completed = set(pd.read_csv(outputfile)['Name'])
        print(f"Found {len(completed)} previously computed knots.")
    except FileNotFoundError:
        completed = set()
        pd.DataFrame(columns=('Name', 'sl3')).to_csv(
            outputfile, index=False
        )

    for i in range(items):

        if names[i] in completed:
            continue

        print(f"{(i/items)*100:.3f}% complete")
        print(f"computing: {names[i]}")

        try:
            computedsl3 = sl3(prepare(pds[i]))

            pd.DataFrame(
                [[names[i], computedsl3]],
                columns=('Name', 'sl3')
            ).to_csv(
                outputfile,
                mode='a',
                header=False,
                index=False
            )

        except Exception as e:
            print(f"Error computing {names[i]}: {e}")

    print("Complete")
    evaluate(outputfile, truthfile)

#===
# Running
main(inputfolder+inputknots, outputfolder+outputsl3s, inputfolder+truthfile)
