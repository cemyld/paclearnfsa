import pygraphviz as pgv


def get_graph(dfa):

    G = pgv.AGraph(strict=False, directed=True, rankdir='LR')

    # set some default node attributes
    G.node_attr['shape'] = 'circle'

    for state, transition_dict in dfa.transitions.items():
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
    G = get_graph(dfa)
    G.layout('dot')
    G.draw(filepath)