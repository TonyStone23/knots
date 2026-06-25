# Input: An open web
# Output: Expansion in terms of the Basis

#===
# Imports
import sympy as sm
from webs import Braid
from printing import basis, display, seebraid

#===
# Variables
#---
# Quantum moves
q = sm.var('q')
quantum2 = sm.var('[2]')
quantum3 = sm.var('[3]')

#---
# Basis Elements
b0, b1, b2, b3, b4, b5 = basis

#===
# ALgorithm subroutines
#---
# resolve a strand
def resolveStrands(web, qweb, verbose = False):
    cycle = False
    newweb = web.copy()
    altered = False

    for item in newweb:
        if len(item) == 2:
            if verbose:
                print("item", item)

            a, b = item
            newweb.remove(item)
            adda = True
            addb = True

            #---
            # Search for a strand, and replace the label not found in a component where a label is found
            for next in newweb:
                if verbose:
                    print("--> next:", next)

                if a in next and adda:
                    addb = False
                    cycle = True
                    newweb.remove(next)
                    newweb.insert(0, [i if a != i else b for i in next])
                    if verbose:
                        print("    --> adding", [i if a != i else b for i in next])
                    altered = True
                
                elif -a in next and adda:
                    addb = False
                    cycle = True
                    newweb.remove(next)
                    newweb.insert(0, [i if -a != i else -b for i in next])
                    if verbose:
                        print("    --> adding", [i if -a != i else -b for i in next])
                    altered = True
                    

                if b in next and addb:
                    adda = False
                    cycle = True
                    newweb.remove(next)
                    newweb.insert(0, [i if b != i else a for i in next])
                    if verbose:
                        print("    --> adding", [i if b != i else a for i in next])
                    altered = True

                if -b in next and addb:
                    adda = False
                    cycle = True
                    newweb.remove(next)
                    newweb.insert(0, [i if -b != i else -a for i in next])
                    if verbose:
                        print("    --> adding", [i if -b != i else -a for i in next])
                    altered = True  

            if verbose:
                print("cycling", cycle)
    
    if cycle:
        if verbose:
            print("cycling on: ", newweb)
        return resolveStrands(newweb, qweb)
    else:
        return newweb, qweb, altered
    
#---
# Resolve strands of three labels
def resolveThreeComponents(web, qweb):

    altered = False

    newweb = web.copy()

    for item in newweb:

        if len(item) == 3:

            a, b, c = item
            newweb.remove(item)
            add = True

            #---
            # The length three component is facing downwards
            if a < 0:
                for next in newweb:
                    if len(next) == 4:
                        w, x, y, z = next

                        if (-a == y) and (-b == x):
                            newweb.remove(next)
                            qweb = qweb * quantum2
                            newweb.insert(0, [-z, -w, c])
                            add = False
                            altered = True

                        elif (b == x) and (c == y):
                            newweb.remove(next)
                            qweb = qweb * quantum2
                            newweb.insert(0, [a, -z, -w])
                            add = False
                            altered = True  
                    
                    elif len(next) == 3:
                        x, y, z, = next

                        if x > 0:
                            pass
                            
                        if (a == x) and (b == y) and (c == z):
                            qweb = qweb * quantum2 * quantum3
                            newweb.remove(next)
                            add = False
                            altered = True
            #---
            # The three component is facing upwards
            if a > 0:
                for next in newweb:
                    if len(next) == 4:
                        w, x, y, z = next

                        if (a == z) and (b == w):
                            newweb.remove(next)
                            qweb = qweb * quantum2
                            newweb.insert(0, [y, x, c])
                            add = False
                            altered = True

                        elif (b == z) and (c == w):
                            newweb.remove(next)
                            qweb = qweb * quantum2
                            newweb.insert(0, [a, y, x])
                            add = False
                            altered = True  
                    
                    elif len(next) == 3:
                        x, y, z, = next

                        if x < 0:
                            pass
                            
                        if (a == x) and (b == y) and (c == z):
                            qweb = qweb * quantum2 * quantum3
                            newweb.remove(next)
                            add = False
                            altered = True

            if add:
                newweb.insert(0, item)
    
    return newweb, qweb, altered

#---
# Resolve a bubble
def resolveBubbles(web, qweb):
    
    altered = False
    newweb = web.copy()

    for item in newweb:

        if len(item) == 4:
            a, b, c, d, = item
            newweb.remove(item)
            add = True

            #---
            # Resolve a bubble on the left
            if d == c:
                qweb = qweb * quantum2
                newweb.insert(0, [a, b])
                altered = True
                add = False
                
            #---
            # Resolve a bubble on the right
            elif a == b:
                qweb = qweb * quantum2
                newweb.insert(0, [d, c])
                altered = True
                add = False
        
            if add:
                newweb.insert(0, item)

    return newweb, qweb, altered

#---
# Resolve a stack case
def resolveStacks(web, qweb):

    altered = False
    newweb = web.copy()

    for item in newweb:

        if len(item) == 4:
            a, b, c, d = item
            newweb.remove(item)
            add = True

            for next in newweb:
                move = False

                if len(next) == 4:
                    w, x, y, z = next

                    #---
                    # Resolve a stack "below" a web
                    if ((a == x) and (d == y)):
                        qweb = qweb * quantum2
                        newweb.remove(next)
                        newweb.insert(0, [w, b, c, z])
                        altered = True
                        move = True
                        add = False
                        
                    #---
                    # Resolve a stack "above" a web
                    elif ((b == w) and (c == z)):
                        qweb = qweb * quantum2
                        newweb.remove(next)
                        newweb.insert(0, [a, x, y, d])
                        altered = True
                        move = True
                        add = False
                
                if move:
                    break

            if add:
                newweb.insert(0, item)

    return newweb, qweb, altered

#---
# Resolve a square case
def resolveSquares(top, bottom, web, qweb):
    
    newweb = web.copy()

    for item in newweb:

        if len(item) == 4:
            a, b, c, d = item
            newweb.remove(item)
            add = True
            
            for next in newweb:

                if len(next) == 4:
                    w, x, y, z = next
                    
                    #---
                    # Resolve a square "above" a web
                    if ((a == x) and (b == w)):
                        newweb.remove(next)
                        return [], qweb * (evaluate(top, bottom, newweb.copy() + [[d, c], [y, z]])
                                              + evaluate(top, bottom, newweb.copy() + [[c, z], [d, y]]))
                    
                    #---
                    # Resolve a square "beneath" a web
                    elif ((d == y) and (c == z)):
                        newweb.remove(next)
                        return [], qweb * (evaluate(top, bottom, newweb.copy() + [[a, b], [w, x]])
                                              + evaluate(top, bottom, newweb.copy() + [[b, w], [a, x]]))
                    
            if add:
                newweb.insert(0, item)

    return newweb, qweb

#---
# Resolve a square with three components
#~~~
# Shell Routine
def resolveThreeSquare(top, bottom, web, qweb, verbose = True):

    newweb = web.copy()

    for first in newweb:

        if len(first) == 4:
            if verbose:
                print(first)

            a, b, c, d = first
            newweb.remove(first)
            addfirst = True
    
            for second in newweb:
                if len(second) == 4:
                    if verbose:
                        print("> ", second)

                    w, x, y, z = second
                    newweb.remove(second)
                    addsecond = True

                    #---
                    # The first case where a square is "on top" of a web
                    if b == z:
                        addthird = True
                        for third in newweb:
                            if len(third) == 4:
                                if verbose:
                                    print("> > ", third)

                                l, m, n, o = third
                                newweb.remove(third)

                                if (a == n) and (w == m):
                                    if verbose:
                                        print("Case 1")
                                        print("recursive call 1: with ", first, second, third)

                                    recurseone = evaluate(top, bottom, newweb.copy() + [[c, y, x], [-d, -o, -l]])
                                    recursetwo = evaluate(top, bottom, newweb.copy() + [[l, x, y, o], [c, d]])
                                    
                                    return [], qweb * (recurseone + recursetwo)

                                if addthird:
                                    newweb.insert(0, third)

                    #---
                    # The second case where a square is "beneath" a web
                    if c == w:
                        addthird = True
                        for third in newweb:
                            if len(third) == 4:
                                if verbose:
                                    print("> > ", third)
                                    
                                l, m, n, o = third
                                newweb.remove(third)

                                if (d == m) and (z == n):
                                    if verbose:
                                        print("Case 2")
                                        print("recursive call 1: with ", first, second, third)

                                    recurseone = evaluate(top, bottom, newweb.copy() + [[-o, -l, -a], [y, x, b]])
                                    recursetwo = evaluate(top, bottom, newweb.copy() + [[l, x, y, o], [a, b]])

                                    return [], qweb * (recurseone + recursetwo)

                                if addthird:
                                    newweb.insert(0, third)

                    if addsecond:
                        newweb.insert(0, second)

            if addfirst:
                newweb.insert(0, first)

    return newweb, qweb

#===
# Main ALgorithm
#---
# Compute a Web
def evaluate(top, bottom, web, verbose = True):

    qweb = 1
    squares = True

    #---
    # Do not check for squares unless the other subroutines have not altered the web
    altered = False

    while web:

        #~~~
        # Check if the web has reduced.
        a, b, c = top
        x, y, z = bottom

        if verbose:
            print("top:", top)
            print("bottom:", bottom)
            print("web ", web)

        #~~~
        # b0 could have up to three components, but none are larger than length 2
        if len(web) <= 3:
            nonstrands = 0
            for item in web:
                if len(item) > 2:
                    nonstrands += 1

                if nonstrands == 0:
                    web = []
                    qweb = qweb * b0

        #~~~
        # Other cases have 1 or two components
        if len(web) <= 2:
            heldwebs = []

            #---
            # count the components of length 4
            for item in web:
                if len(item) == 4:
                    heldwebs.append(item)
                
            # One web forms a basis
            if len(heldwebs) == 1:
                l, m, n, o = heldwebs[0]

                if (o == y) and (l == z):
                    web = []
                    qweb = qweb * b1

                elif (o == x) and (l == y):
                    web = []
                    qweb = qweb * b2
        
            # Two webs form a basis
            elif len(heldwebs) == 2:
                l, m, n, o = heldwebs[0]
                q, r, s, t = heldwebs[1]
                
                if q == n:
                    web = []
                    qweb = qweb * b3

                elif o == r:
                    web = []
                    qweb = qweb * b3

                elif t == m:
                    web = []
                    qweb = qweb * b4

                elif l == s:
                    web = []
                    qweb = qweb * b4

            #---
            # Remaining components must be 'pitchforks'
            if len(heldwebs) == 0:
                web = []
                qweb = qweb * b5

        #~~~
        # Resolve strands
        if verbose:
            print("before resolve strands")
            print(f"    qweb: {qweb} --- web: {web}")

        web, qweb, altered = resolveStrands(web, qweb)
        if altered:
            squares = False

        if verbose:
            print("after resolve strands")
            print(f"    qweb: {qweb} --- web: {web}\n")

        #---
        # Resolve stacks
        if verbose:
            print("before resolve stacks")
            print(f"    qweb: {qweb} --- web: {web}")

        web, qweb, altered = resolveStacks(web, qweb)
        if altered:
            squares = False
        
        if verbose:
            print("after resolve stacks")
            print(f"    qweb: {qweb} --- web: {web}\n")

        #---
        # Resolve bubbles
        if verbose:
            print("before resolve bubble")
            print(f"    qweb: {qweb} --- web: {web}")

        web, qweb, altered = resolveBubbles(web, qweb)
        if altered:
            squares = False

        if verbose:
            print("after resolve bubble")
            print(f"    qweb: {qweb} --- web: {web}\n")

        #---
        # Resolve components of three
        if verbose:
            print("before resolve squares of three")
            print(f"    qweb: {qweb} --- web: {web}")

        web, qweb, altered = resolveThreeComponents(web, qweb)
        if altered:
            squares = False

        if verbose:
            print("after resolve squares of three")
            print(f"    qweb: {qweb} --- web: {web}\n")

        #~~~
        # Resolve squares of three components   
        if squares and (len(web) >= 3):

            if verbose:
                print("before resolve squares of three")
                print(f"    qweb: {qweb} --- web: {web}")

            web, qweb = resolveThreeSquare(top, bottom, web, qweb)

            if verbose:
                print("after resolve squares of three")
                print(f"    qweb: {qweb} --- web: {web}\n")
        
        #---
        # For next loop
        squares = True

    return qweb

#===
# Main Method
def main(braid, showinput = True):

    top, bottom, web = braid
    if showinput:
        print("\nInput Braid:")
        seebraid(top, bottom, web)

    print("\nEvaluated ouput:")
    display(evaluate(top, bottom, web))


if __name__ == '__main__':
    main(Braid.braid02, False)
