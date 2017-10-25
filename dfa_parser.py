import DFA

'''
{
    'accepts': {}
    'start' : ''
    'transitions': { state: {token:next_state, ...}, ...}
    EXAMPLE:
    {'accepts': {1},
     'start': {0},
     'transitions': {0: {0: 0, 1: 1}, 1: {0: 1, 1: 0}}}
}
'''
def dfa_from_dict(dc):
    accepts = set(dc['accepts'])
    start = dc['start']
    transitions = dc['transitions']
    states = transitions.keys()
    alphabet = {token for state in transitions for token in transitions[state]}
    return DFA.DFA(states=states, alphabet=alphabet, transitions=transitions, start=start, accepts=accepts)
def dfa_to_dict(dfa):
    dct = {}
    dct['accepts'] = dfa.accepts
    dct['start'] = dfa.start
    dct['transitions'] = dfa.transitions
    return dct
