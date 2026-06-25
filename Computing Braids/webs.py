#===
# Braids
#---
# PD Code convention:

# Unclosed braids contain a tuple: (top, bottom, web).

    # top := the three exiting labels.

    # bottom := the three exiting labels.

    # web := PD code of the web.

#===
# Braid class to serve as pointers to pre-defined braids 
class Braid:
    #---
    # Basis Element Definition
    b0 = ([1, 2, 3],
          [1, 2, 3],
          [])
    
    b1 = ([1, 4, 5],
          [1, 2, 3],
          [[3, 5, 4, 2]])
    
    b2 = ([4, 5, 3],
          [1, 2, 3],
          [[2, 5, 4, 1]])
    
    b3 = ([5, 6, 7],
          [1, 2, 3],
          [[2, 4, 5, 1], [3, 7, 6, 4]])
    
    b4 = ([5, 6, 7],
          [1, 2, 3],
          [[3, 7, 4, 2], [4, 6, 5, 1]])
    
    b5 = ([4, 5, 6],
          [1, 2, 3],
          [[-1, -2, -3], [4, 5, 6]])
    
    #---
    # Other Braids
    braid01 = ([5, 6, 9],
            [1, 2, 3],
            [[2, 4, 5, 1], [3, 9, 6, 4]])

    braid02 = ([7, 11, 10],
            [1, 2, 3],
            [[9, 10, 11, 8], [6, 8, 7, 5], [3, 9, 6, 4], [2, 4, 5, 1]])

#===
# Compute the composition of two braids

    # Needs improvement, composition with components of 3 needs attention.
def compose(w2, w1):
    """
    **Input**: The tuple representing a braid: (top, bottom, web)
    
    **Output**: The composisiton of braids. 

    *Please note that the input order matters*         
    """

    top1, bottom1, web1 = w1
    top2, bottom2, web2 = w2

    bump = max([max(x) for x in web2] + [max(top2)] + [max(bottom2)])
    relabelledweb = [[x + bump for x in component] for component in web1]
    top1 = [x + bump for x in top1]
    bottom1 = [x + bump for x in bottom1]

    a, b, c = bottom1
    subbeda = False
    subbedb = False
    subbedc = False
    x, y, z = top2

    while not (subbeda and subbedb and subbedc):
        
        #---
        # Check labels in the web
        if relabelledweb:
            item = relabelledweb.pop(0)
            add = True

            if a in item:
                relabelledweb.append([i if i != a else x for i in item])
                subbeda = True
                add = False

            elif b in item:
                relabelledweb.append([i if i != b else y for i in item])
                subbedb = True
                add = False

            elif c in item:
                relabelledweb.append([i if i != c else z for i in item])
                subbedc = True
                add = False

            if add:
                relabelledweb.append(item)
        
        #---
        # Check labels in the top strand

        if a in top1:
            top1 = [i if i != a else x for i in top1]
            subbeda = True
            add = False

        elif b in top1:
            top1 = [i if i != b else y for i in top1]
            subbedb = True
            add = False

        elif c in top1:
            top1 = [i if i != c else z for i in top1]
            subbedc = True
            add = False

    return (top1, bottom2, relabelledweb + web2)