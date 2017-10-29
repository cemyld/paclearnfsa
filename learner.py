import DFA.DFA as DFA


def merge(state1, state2, dfa):
    '''
    Merges state2 into state1 and removes state2
    '''
    transitions = dfa.transitions
    for s in dfa.states:
        if s in transitions:
            for token in transitions[s]:
                if state2 in transitions[s][token]:
                    transitions[s][token] = state1
        if state2 in transitions:
            for token in transitions[state2]:
                if s in transitions[state2][token]:
                    transitions[state1][token] = s
    if dfa.start == state2:
        dfa.start = state1
    if state2 in dfa.accepts:
        dfa.accepts = dfa.accepts.difference({state2}).union({state1})
    if state2 in transitions:
        del transitions[state2]
    dfa.states.remove(state2)
    dfa.transitions = transitions
    return dfa


def check_rejects(dfa, neg_examples):
    for neg_ex in neg_examples:
        if dfa.recognizes(neg_ex):
            return False
    return True

def get_state_order(dfa):
    levels = dfa.levels()

    levelsDict = {}

    levels.pop('sink', None)

    for key in levels:
        if not levels[key] in levelsDict:
            levelsDict[levels[key]] = [key]
        else:
            levelsDict[levels[key]].append(key)
        levelsDict[levels[key]].sort()

    output = []
    for level in sorted(levelsDict):
        for value in levelsDict[level]:
            output.append(value)

    return output


def rpni_promote(dfa, reds, blues, state):
    reds.add(state)
    blues.remove(state)
    for token, state in dfa.transitions[state]:
        blues.add(state)
    return dfa, reds, blues

def rpni_fold(dfa, red_state, blue_state):
    '''folds blue_state into red_state'''
    if blue_state in dfa.accepts:
        dfa.accepts.add(red_state)
    for token in dfa.alphabet:
        if
def rpni_merge(dfa, red_state, blue_state):
    for state, state_trans in dfa.transitions:
        for token, next_state in state_trans:
            if next_state == blue_state:
                dfa.transitions[state][token] = red_state
    return rpni_fold(dfa, red_state, blue_state)
def learn_dfa(teacher, num_examples):
    # binary alphabet
    alphabet = ['a', 'b']
    for i in range(num_examples):
        teacher.example()
    examples = teacher.used_examples
    pos_examples = [ex[0] for ex in examples if ex[1] == '+']
    neg_examples = [ex[0] for ex in examples if ex[1] == '-']
    pta = DFA.from_word_list(pos_examples, alphabet)
    return pta
