#===
# Imports
from pathlib import Path

from braid import sl3
from webs import Braid, power
import pandas as pd

header = "Computing Braids/output/"


def computeGarsidePowers(n):
    """
    Compute the powers of the Garside element from 1 to n.

    Progress is saved after every completed computation so the script
    can be interrupted and resumed.
    """

    outputfile = Path(header) / f"garside_1:{n}.csv"

    # Load previous progress if it exists
    if outputfile.exists():
        output = pd.read_csv(outputfile)
        completed = {
            int(name.split("^")[1])
            for name in output["garside^n"]
        }
        print(f"Loaded {len(completed)} completed computations.")
    else:
        output = pd.DataFrame(columns=("garside^n", "sl3"))
        completed = set()

    for i in range(1, n + 1):

        if i in completed:
            print(f"Skipping garside^{i}")
            continue

        print(f"Computing garside^{i} ({i}/{n})")

        braid = power(Braid.garside, i)
        computed = sl3(braid, False)

        output.loc[len(output)] = [f"garside^{i}", computed]

        # Save checkpoint immediately
        output.to_csv(outputfile, index=False)

        print(f"Saved garside^{i}")

    print("Finished.")