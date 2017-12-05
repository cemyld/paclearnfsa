import DFA.DFA as DFA
import random
import dfa_parser as DFAParser


max_iter_counter = 2000


class Teacher:

    def __init__(self, dfa):
        self.dfa = dfa
        self.used_examples = set()

    def _randstring(self, length=1):
        return ''.join(random.choice(tuple(self.dfa.alphabet)) for _ in range(length))

    def _get_new_example(self):
        # after generating, does not add to used examples
        # longest_len = self.dfa.longest_word_length()
        longest_len = 2*len(self.dfa.states)
        example_len = random.randint(1, longest_len)
        # iterate until new example is found, there is a counter to break infinite loops
        counter = 0
        example_str = self._randstring(example_len)
        while example_str in self.used_examples:
            example_str = self._randstring(example_len)
            counter += 1
            if counter > max_iter_counter:
                raise Exception(
                    'While iterating through random strings, no NEW example could be made in {} attempts'.format(counter))

        if self.dfa.recognizes(example_str):
            return(example_str, '+')
        else:
            return(example_str, '-')

    def example(self):
        example_str, label = self._get_new_example()
        # add to used examples
        self.used_examples.add((example_str, label))
        return(example_str, label)

    def get_pos_example(self):
        example_str, label = self._get_new_example()
        # iterate until positive example is found, there is a counter to break infinite loops
        counter = 0
        while label == '-':
            example_str, label = self._get_new_example()
            counter += 1
            if counter > max_iter_counter:
                raise Exception(
                    'While iterating through random strings, no POSITIVE example could be made in {} attempts'.format(counter))
        # add to used examples
        self.used_examples.add((example_str, label))
        return(example_str, label)

    def get_neg_example(self):
        example_str, label = self._get_new_example()
        # iterate until negative example is found, there is a counter to break infinite loops
        counter = 0
        while label == '+':
            example_str, label = self._get_new_example()
            counter += 1
            if counter > max_iter_counter:
                raise Exception(
                    'While iterating through random strings, no NEGATIVE example could be made in {} attempts'.format(counter))
        # add to used examples
        self.used_examples.add((example_str, label))
        return(example_str, label)

    def get_label(self, example_str):
        if self.dfa.recognizes(example_str):
            return '+'
        else:
            return '-'


    # generate |T(A)|
    def construct_char_set(self):
        '''Construct a characteristic set of the DFA, TODO'''

        tree = self.construct_tree()
        start_node = tree[-1]
        degree = self.degree(start_node)
        char_set = []
        self.paths(start_node, '', '', char_set)

        return list(filter(None, char_set))
    
    def paths(self, start, string ,trans, char_set):
        string += trans
        if len(start.children) == 0:
            char_set.append(string)
            return

        for k, v in start.children.items():
            if string not in char_set:
                char_set.append(string)

            self.paths(v, string, k, char_set)

                
    def construct_tree(self):
        '''Construct a tree T of given DFA'''

        checked = []
        unchecked = []
        node_list = []
        start = Node(self.dfa.start)
        unchecked.append(start.state)
        self.construct_tree_rec(start, checked, unchecked, node_list)
        return node_list 


    def construct_tree_rec(self, node, checked, unchecked, node_list):
        '''recursive part'''
        if len(unchecked) == 0:
            return

        unchecked.remove(node.state)
        checked.append(node.state)

        for alph in self.dfa.alphabet:
            child = self.dfa.delta(node.state, alph)
            if child == "sink":
                continue
            elif child in checked:
                node.add_child(alph, Node(child))
            else:
                unchecked.append(child)
                node.add_child(alph, self.construct_tree_rec(Node(child), checked, unchecked, node_list))
                
        
        node_list.append(node)
        return node
    
    def degree(self, tree):
        if len(tree.children) == 0:
            return 1

        children_depth = []
        
        for k, node in tree.children.items():
            children_depth.append(self.degree(node))

        return max(children_depth) + 1

class Node(object):
    def __init__(self, state):
        self.state = state
        self.children = {}

    def add_child(self, trans, obj):
        self.children[trans] = obj


def recursive_print_tree(node, trans, depth=0):
    print('   ' * depth + trans + ': ' + str(node.state))
    for k, v in node.children.items():
        recursive_print_tree(v, k, depth+1)


if __name__ == '__main__':
    dfa = DFAParser.from_dict(
    {'accepts': {2},
    'start': 0,
    'transitions': {0: {'a': 1  , 'b': 1}, 1: {'a': 0, 'b': 2}, 2: {'a': 2, 'b': 0}}}
    )
    
    teacher = Teacher(dfa)
    tree = teacher.construct_tree()
    print("Degree: " + str(teacher.degree(tree[-1])))
    recursive_print_tree(tree[-1], 'st')

    print(teacher.construct_char_set())