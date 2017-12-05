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

    def construct_char_set(self):
        '''Construct a characteristic set of the DFA, TODO'''
        return

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
                node.add_child({alph: child})
            else:
                unchecked.append(child)
                node.add_child({alph: child})
                self.construct_tree_rec(Node(child), checked, unchecked, node_list)
        
        node_list.append(node)
            



class Node(object):
    def __init__(self, state):
        self.state = state
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)




if __name__ == '__main__':
    dfa = DFAParser.from_dict(
    {'accepts': {2},
    'start': 0,
    'transitions': {0: {'a': 1  , 'b': 1}, 1: {'a': 0, 'b': 2}, 2: {'a': 2, 'b': 0}}}
    )
    
    teacher = Teacher(dfa)
    tree = teacher.construct_tree()
    for node in tree:
        print(node.state)
        print(node.children)