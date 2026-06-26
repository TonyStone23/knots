# Knots

Computations relating to the sl3 invariant from the PD code representation of a knot or link.

## Project Components

### Computing sl3/

- **statesum.py**

    - This file contains the algorithm to compute the sl3 invariant of knots and links.

- **compute.py**

    - This file is used to compute large amounts of knots/links. 

    - File parameters recorded and input from **trials.py**.

- **data.py**

    - This file contains the tools to manage knot datasets. 

    - Can be used to generate a set with RI invariants applied to them.

- **trials.py**

    - This file contains paths to individual files.

    - This file contains the names of required input and output csv files.

- **input/output**

    - These folders contain csv files that are used for inputs and output. 

        - Any file that is an input to another process goes into "input".
        - Computed sl3s go into "output".

    - File names should be recorded in **trials.py**.

### Computing Braids/

- **braids.py**

    - This file has the computation which reduces an unclosed braid to a linear combination of basis elements.

- **webs.py**

    - This file contains the definitions for the basis elements, and other braids.

        - Convention for definint a braid is included
    
    - This file contains the function definition to compose two braids.

- **prinitng.py**

    - This file contains the tools in order to display braids and basis elements.

- **reference.py**

    - This file serves as the shell for running a braid computation.

- **sandbox.py**

    - This file serves as a sandbox for braid computation

## Development Timeline

- **May 2026 - July 2026.** Work done within the suriem program SURIEM REU at MSU.

    - May 18 - Program begins.

    - June 20-22 -  computedknots.csv is generated using the <a href = "https://docs.icer.msu.edu/">HPCC</a> at MSU.

## Acknowledgements

Thank you to my SURIEM Mentor Matthew Harper for consultation with code development. Thank you to my teammates, Josh O'connor, Pepe Sanchez-Menchen, and Angie Wu for support. Thank you to the SURIEM Program as a whole for friendship!

## Citations

[1] M. Harper and E. Kalfagianni, _On the quantum sl3 invariant of positive links_, <a href = https://arxiv.org/abs/2508.15153>arXiv:2508.15153</a>, June 16, 2026.

[2] T. Ohtsuki, _Quantum Invariants: A Study of Knots, 3-manifolds, and Their Sets_, <a href = "https://books.google.com/books?id=KGdqDQAAQBAJ">books.google.com</a>, June 17, 2026


[3] C. Livingston and A. H. Moore, KnotInfo: Table of Knot Invariants, <a href = https://knotinfo.org>knotinfo.org</a>, June 16, 2026. 

[4] Institute for Cyber-Enabled Research at Michigan State University, _High Performance Computing Center_, <a href = "https://docs.icer.msu.edu/"> ICER Documentation</a>, June 20, 2026.