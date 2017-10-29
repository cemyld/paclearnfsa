import DFA.DFA as DFA

'''
{'accepts': {}
'start' : ''
'transitions': { state: {token:next_state, ...}, ...}
EXAMPLE:
{'accepts': {1},
 'start': {0},
 'transitions': {0: {0: 0, 1: 1}, 1: {0: 1, 1: 0}}}
'''


def dfa_from_dict(dct):
    accepts = set(dct['accepts'])
    start = dct['start']
    transitions = dct['transitions']
    states = {state for state_transitions in transitions.values() for state in state_transitions.values()}.union(set(transitions.keys()))
    alphabet = {token for state_transitions in transitions.values() for token in state_transitions.keys()}
    return DFA.DFA(states=states, alphabet=alphabet, transitions=transitions, start=start, accepts=accepts)


def dfa_to_dict(dfa):
    dct = {}
    dct['accepts'] = dfa.accepts
    dct['start'] = dfa.start
    dct['transitions'] = dfa.transitions
    return dct
