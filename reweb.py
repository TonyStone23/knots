pd = [[2, 14, 3, 13], [7, 13, 8, 12], [15, 5, 16, 4],[3, 9, 4, 8], [6, 2, 7, 1], [14, 10, 15, 9], [10, 6, 11, 5], [11, 1, 12, 16],]

def resolveThreeSquare(state, verbose = False):

    traveled = False
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

                    #---
                    # The first case where a square is "on top" of a web
                    if b == z:
                        addthird = True
                        for third in newState:
                            if len(third) == 4:
                                l, m, n, o = third
                                newState.remove(third)

                                if (a == n) and (w == m):
                                    if verbose:
                                        print("Case 1")
                                        print("recursive call 1: with ", first, second, third)

                                    return travelWebs([x, y, c], [l, o, d], newState, 1)
                                
                                if addthird:
                                    newState.insert(0, third)

                    #---
                    # The second case where a square is "beneath" a web
                    if c == w:
                        addthird = True
                        for third in newState:
                            if len(third) == 4:
                                l, m, n, o = third
                                newState.remove(third)

                                if (d == m) and (z == n):
                                    if verbose:
                                        print("Case 2")
                                        print("recursive call 1: with ", first, second, third)

                                    return travelWebs([o, l, a], [y, x, b], newState, 2)

                                if addthird:
                                    newState.insert(0, third)

                    if addsecond:
                        newState.insert(0, second)

            if addfirst:
                newState.insert(0, first)

    return

#~~~
# Travel webs
def travelWebs(start, end, state, case, verbose = True):

    if verbose:
        print("travelling: ", state)
        print("start: ", start)
        print("end: ", end)

    a, b, c = start
    x, y, z = end

    newState = state.copy()
    generatedWeb = []

    travel = True

    #---
    # Handle the first case
    if case == 1:
        while travel:
            item = newState.pop()
            add = True

            if len(item) == 4:
                q, r, s, t = item

                print(a, q)

                if a == q:
                    add = False
                    generatedWeb.append([t, b, c, q])
                    a = r
                    b = s
                    c = q

                elif a == t:
                    add = False
                    generatedWeb.append([t, b, c, q])
                    a = r
                    b = s
                    c = t

                if a == x:
                    generatedWeb.append([y, b, c, z])
                    travel = False
                
                if add:
                    newState.insert(0, item)

    #---
    # Handle the second case   
    if case == 2:
        while travel:
            item = newState.pop()
            add = True

            if len(item) == 4:
                q, r, s, t = item

                if a == s:
                    add = False
                    generatedWeb.append([c, s, r, b])
                    a = t
                    b = q
                    c = s

                elif a == r:
                    add = False
                    generatedWeb.append([c, s, r, b])
                    a = t
                    b = q
                    c = r

                if t == x:
                    generatedWeb.append([c, z, y, b])
                    travel = False
                
                if add:
                    newState.insert(0, item)    
                
    return newState + generatedWeb


print(resolveThreeSquare(pd, True))