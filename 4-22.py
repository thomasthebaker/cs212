# -----------------
# User Instructions
# 
# Write a function, csuccessors, that takes a state (as defined below) 
# as input and returns a dictionary of {state:action} pairs. 
#
# A state is a tuple with six entries: (M1, C1, B1, M2, C2, B2), where 
# M1 means 'number of missionaries on the left side.'
#
# An action is one of the following ten strings: 
#
# 'MM->', 'MC->', 'CC->', 'M->', 'C->', '<-MM', '<-MC', '<-M', '<-C'
# where 'MM->' means two missionaries travel to the right side.
# 
# We should generate successor states that include more cannibals than
# missionaries, but such a state should generate no successors.

def csuccessors(state):
    """Find successors (including those that result in dining) to this
    state. But a state where the cannibals can dine has no successors."""
    M1, C1, B1, M2, C2, B2 = state
    items = []
    if (C1>M1 or C2>M2): return {}
    if (B1>0):
        #for every single combo and double combo
        if C1>0: items+=[((M1,C1-1,B1-1,M2,C2+1,B2+1),'C->')]
        if M1>0: items+=[((M1-1,C1,B1-1,M2+1,C2,B2+1), 'M->')]
        if M1>1: items+=[((M1-2,C1,B1-1,M2+2,C2,B2+1), 'MM->')]
        if C1>1: items+=[((M1,C1-2,B1-1,M2,C2+2,B2+1), 'CC->')]
        if (C1>0 and M1>0): items+=[((M1-1,C1-1,B1-1,M2+1,C2+1,B2+1), 'MC->')]
    elif (B2>0):
        if C2>0: items+=[((M1,C1+1,B1+1,M2,C2-1,B2-1), '<-C')]
        if M2>0: items+=[((M1+1,C1,B1+1,M2-1,C2,B2-1), '<-M')]
        if M2>1: items+=[((M1+2,C1,B1+1,M2-2,C2,B2-1), '<-MM')]
        if C2>1: items+=[((M1,C1+2,B1+1,M2,C2-2,B2-1), '<-CC')]
        if (C2>0 and M2>0): items+=[((M1+1,C1+1,B1+1,M2-1,C2-1,B2-1), '<-MC')]
    result = dict(items)
    print(result)
    return result
        

def test():
    assert csuccessors((2, 2, 1, 0, 0, 0)) == {(2, 1, 0, 0, 1, 1): 'C->', 
                                               (1, 2, 0, 1, 0, 1): 'M->', 
                                               (0, 2, 0, 2, 0, 1): 'MM->', 
                                               (1, 1, 0, 1, 1, 1): 'MC->', 
                                               (2, 0, 0, 0, 2, 1): 'CC->'}
    assert csuccessors((1, 1, 0, 4, 3, 1)) == {(1, 2, 1, 4, 2, 0): '<-C', 
                                               (2, 1, 1, 3, 3, 0): '<-M', 
                                               (3, 1, 1, 2, 3, 0): '<-MM', 
                                               (1, 3, 1, 4, 1, 0): '<-CC', 
                                               (2, 2, 1, 3, 2, 0): '<-MC'}
    assert csuccessors((1, 4, 1, 2, 2, 0)) == {}
    return 'tests pass'

print (test())
