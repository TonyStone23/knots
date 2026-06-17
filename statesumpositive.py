# Compute the state sum of a knot or link
# Input: Positive not or link
# Output: State Sum

# Works for all positive knots on knotinfo.

#===
# Imports
import sympy as sm

#===
# Quantum moves
q = sm.var('q')
quantum2 = sm.var('[2]')
quantum3 = sm.var('[3]')

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
                    
                elif (b == y) or (d == z) or (d == w) or (d == x):
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
# Crossing Moves
#---
# O move
def Omove(signedentry):
    crossing, sign = signedentry
    a, b, c, d = crossing

    if sign == 'positive':
        return [[a, b], [d, c]], q**(-2)
    else:
        return [[a, d], [b, c]], q**(2)
    
#---
# W move
def Wmove(signedentry):
    crossing, sign = signedentry

    if sign == 'positive':
        return [crossing], -q**(-3)
    else:
        a, b, c, d = crossing
        return [[b, c, d, a]], -q**3

#===
# Evaluating a diagram
#---
# Find all of the states
def findStates(signedpd, verbose = False):

    if len(signedpd) == 1:
        return (Omove(signedpd[0]), Wmove(signedpd[0]))
    
    results = findStates(signedpd[1:])
    returns = []

    for result in results:
        state, phi = result

        omove, ophi = Omove(signedpd[0])
        wmove, wphi = Wmove(signedpd[0])

        returns.append((omove + state, phi * ophi))
        returns.append((wmove + state, phi * wphi))

    return returns

#~~~
# resolve a strand
def resolveStrands(state, qState):
    cycle = False
    newState = state.copy()

    for item in newState:
        if len(item) == 2:
            a, b = item
            newState.remove(item)

            adda = True
            addb = True

            for next in newState:
                if a in next and adda:
                    addb = False
                    cycle = True
                    newState.remove(next)
                    newState.insert(0, [i if a != i else b for i in next])
                    break

                if b in next and addb:
                    adda = False
                    cycle = True
                    newState.remove(next)
                    newState.insert(0, [i if b != i else a for i in next])
                    break

            if adda and addb:
                qState = qState * quantum3
    
    if cycle:
        return resolveStrands(newState, qState)
    else:
        return newState, qState
    
#~~~
# Count the strands
def countStrands(state):
    webs = 0
    strands = 0
    for item in state:
        if len(item) == 2:
            strands += 1
        else:
            webs += 1
    return webs, strands

#~~~
# Resolve a bubble
def resolveBubbles(state, qState):
    
    newState = state.copy()
    for item in newState:

        if len(item) == 4:
            a, b, c, d, = item
            newState.remove(item)
            add = True

            if d == c:
                qState = qState * quantum2
                newState.insert(0, [a, b])
                add = False
                
            elif a == b:
                qState = qState * quantum2
                newState.insert(0, [d, c])
                add = False
        
            if add:
                newState.insert(0, item)

    return newState, qState

#~~~
# Resolve a stack case
def resolveStacks(state, qState):
    
    newState = state.copy()
    for item in newState:

        if len(item) == 4:
            a, b, c, d = item
            newState.remove(item)
            
            add = True
            for next in newState:
                move = False

                if len(next) == 4:
                    w, x, y, z = next

                    if ((a == x) and (d == y)):
                        qState = qState * quantum2
                        newState.remove(next)
                        newState.insert(0, [w, b, c, z])
                        move = True
                        add = False

                    elif ((b == w) and (c == z)):
                        qState = qState * quantum2
                        newState.remove(next)
                        newState.insert(0, [a, x, y, d])
                        move = True
                        add = False
                
                if move:
                    break

            if add:
                newState.insert(0, item)

    return newState, qState

#~~~
# Resolve a square case
def resolveSquares(state, qState):
    
    newState = state.copy()
    for item in newState:

        if len(item) == 4:
            a, b, c, d = item
            newState.remove(item)

            add = True
            
            for next in newState:

                if len(next) == 4:
                    w, x, y, z = next
                    
                    if ((a == x) and (b == w)):
                        newState.remove(next)
                        #print(newState + [[d, c], [y, z]])
                        return [], qState * (evaluateState(newState.copy() + [[d, c], [y, z]])
                                              + evaluateState(newState.copy() + [[c, z], [d, y]]))
                    
                    elif ((d == y) and (c == z)):
                        newState.remove(next)
                        return [], qState * (evaluateState(newState.copy() + [[a, b], [w, x]])
                                              + evaluateState(newState.copy() + [[b, w], [a, x]]))
                
                    
            if add:
                newState.insert(0, item)

    return newState, qState

#===
# Resolve a square with three components # ACCOUNT FOR WEB FLIPPINGS
#---
# Shell Routine
def resolveThreeSquare(state, qState):

    newState = state.copy()
    for first in newState:

        if len(first) == 4:
            a, b, c, d = first
            newState.remove(first)
            addfirst = True
    
            for second in newState:
                if len(second) == 4:
                    w, x, y, z = second
                    newState.remove(second)
                    addsecond = True

                    if b == z:
                        addthird = True
                        for third in newState:
                            if len(third) == 4:
                                l, m, n, o = third
                                newState.remove(third)

                                if (a == n) and (w == m):
                                    addfirst = False
                                    addsecond = False
                                    addthird = False
                                    #print("recursive call on: ", newState + [first] + [second] + [third])
                                    #print("recursive call 1: with ", first, second, third)
                                    recurseone = evaluateState(travelWebs([l, o, d], [x, y, c], newState))
                                    #print("recursive call 2: with ", first, second, third, [l,x,y,o])
                                    recursetwo = evaluateState(newState.copy() + [[l, x, y, o],  [c, d]])
                                    return [], qState * (recurseone + recursetwo)

                                if addthird:
                                    newState.insert(0, third)
                
                    if addsecond:
                        newState.insert(0, second)

            if addfirst:
                newState.insert(0, first)

    return newState, qState

#---
# Travel webs
def travelWebs(start, end, state, verbose = False):

    # print("travelling: ", state)
    # print("start: ",start)
    # print("end: ", end)

    a, b, c = start
    x, y, z = end
    
    newState = state.copy()

    foundpath = False
    path = []

    # find path
    while not foundpath:
        if verbose:
            print(newState)
        item = newState.pop(0)
        if len(item) == 4:
            l, m, n, o = item
            if verbose:
                print("path: ", path)

            if a == m:
                path.append(item)
                if x == l:
                    foundpath = True
                else: 
                    a = l
            
            else:
                newState.append(item)
        else:
            newState.append(item)

    #print("state before webs: ", newState)
    for web in path: 

        print(web)

        l, m, n, o = web

        newState.append([b, n, m, c])
        b = o
        c = m
        if l == x: 
            newState.append([o, y, z, c])

    #print("Newly constructed state:", newState)
    return newState

#---
# Compute lLWll(s)
def evaluateState(state, verbose = False):
    qState = 1
    while state:
        if verbose:
            print("resolve strands")
            print(f"qState: {qState} --- State: {state}")
        state, qState = resolveStrands(state, qState)

        # Resolve bubbles
        if verbose:
            print("resolve bubble")
            print(f"qState: {qState} --- State: {state}")
        state, qState = resolveBubbles(state, qState)

        # Resolve stacks
        if verbose:
            print("resolve stacks")
            print(f"qState: {qState} --- State: {state}")
        state, qState = resolveStacks(state, qState)

        # Resolve Squares
        if verbose:
            print("resolve squares of two")
            print(f"qState: {qState} --- State: {state}")
        state, qState = resolveSquares(state, qState)

        # Resolve Squares
        webs, strands = countStrands(state)
        if (strands == 0) and (webs > 0):
            if verbose:
                print("resolve squares of three")
                print(f"qState: {qState} --- State: {state}")
            state, qState = resolveThreeSquare(state, qState)

    return qState

#---
# Compute phi(s)
def phase(state):
    
    ws = sum([1 if len(i) == 4 else 0 for i in state])
    os = (len(state) - ws)//2

    return q**((-1) *os * 2) * (-q)**((-1) * ws * 3)

#---
# Perform State Sum
def stateSum(pd, verbose = False):

    # Determine states
    signedpd = positivity(pd)
    states = findStates(signedpd)

    # Compute y(s)
    ys = []
    for i in range(len(states)):
        #print("Computing state ", i)
        state, phi = states[i]
        llWll = evaluateState(state)
        ys.append(phi * llWll)

        if verbose:
            print("State: ", i)
            print(ys[-1])

    # Summate over y(s)s
    llDll = 0
    for y in ys:
        llDll += y

    if verbose:
        print("")
        print("--- Evaluation ---")
        print(f"llDll = {llDll}")
        print("")
    
    return llDll

#---
# Simplify sl3
def simplify(llDll):
    q2 = (q + q**(-1))
    q3 = (q**2 + 1 + q**(-2))
    return llDll.subs({quantum2:q2, quantum3:q3}).expand()

#===
# Compute the sl3 polynomial
def sl3(pd):
    llDll = stateSum(pd)
    simplified = simplify(llDll)
    return simplified

#---
# Compute a state
def evaluateOne(pd, i):
    state = findStates(positivity(pd))[i]
    web, phase = state
    evaluateState(web)

#===
# Testing
pd_9_32 = [[2,8,3,7],[4,9,5,10],[6,13,7,14],[8,16,9,15],[10,5,11,6],[12,17,13,18],[14,3,15,4],[16,2,17,1],[18,11,1,12]]
pd_9_30 = [[1,9,2,8],[3,16,4,17],[5,1,6,18],[7,12,8,13],[9,3,10,2],[11,6,12,7],[13,10,14,11],[15,4,16,5],[17,15,18,14]]
pd_9_27 = [[2,9,3,10],[4,7,5,8],[6,14,7,13],[8,15,9,16],[10,18,11,17],[12,3,13,4],[14,6,15,5],[16,2,17,1],[18,12,1,11]]
pd_9_21 = [[2,7,3,8],[4,13,5,14],[6,15,7,16],[8,12,9,11],[10,17,11,18],[12,5,13,6],[14,3,15,4],[16,2,17,1],[18,9,1,10]]
pd_8_21 = [[1,7,2,6],[4,13,5,14],[5,9,6,8],[7,3,8,2],[9,13,10,12],[11,1,12,16],[14,3,15,4],[15,11,16,10]]
pd_8_18 = 	[[6,2,7,1],[8,3,9,4],[16,11,1,12],[2,14,3,13],[4,15,5,16],[10,6,11,5],[12,7,13,8],[14,10,15,9]]
pd_11a_266 = [[6,2,7,1],[10,3,11,4],[14,7,15,8],[18,11,19,12],[12,6,13,5],[4,18,5,17],[20,16,21,15],[16,10,17,9],[22,13,1,14],[2,19,3,20],[8,21,9,22]]

if __name__ == '__main__':
    print(sl3(pd_9_21))
    #evaluateOne(pd_11a_266, 2047)