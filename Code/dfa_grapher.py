import sys
try:
    import pygraphviz as pgv
except Exception as e:
    print("Could not import pygraphviz library, will continue without graphing function.")


def get_graph(dfa):
    if not 'pygraphviz' in sys.modules:
        return

    G = pgv.AGraph(strict=False, directed=True, rankdir='LR')

    # set some default node attributes
    G.node_attr['shape'] = 'circle'

    for state, transition_dict in dfa.transitions.items():
        if state == 'sink':
            continue
        # add node
        G.add_node(state)
        # add edges
        for token, next_state in transition_dict.items():
            G.add_edge(state, next_state, label=token)

    # add starting state
    n = G.get_node(dfa.start)
    n.attr['style'] = 'bold'
    # add accepting states
    for accepted_state in dfa.accepts:
        n = G.get_node(accepted_state)
        n.attr['shape'] = 'doublecircle'
    return G


def draw_dfa(dfa, filepath='dfa_graph.png'):
    if not 'pygraphviz' in sys.modules:
        return
    G = get_graph(dfa)
    G.layout('dot')
    G.draw(filepath)

def draw_dfa_colored(dfa, reds, blues, filepath='dfa_graph.png'):
    if not 'pygraphviz' in sys.modules:
        return
    G = get_graph(dfa)

    #colorize reds
    for state in reds:
        n = G.get_node(state)
        n.attr['color'] = 'red'
    #colorize blues
    for state in blues:
        n = G.get_node(state)
        n.attr['color'] = 'blue'
    G.layout('dot')
    G.draw(filepath)
