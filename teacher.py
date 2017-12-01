import DFA.DFA as DFA
import random


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

    def construct_T(self):
        '''Construct a tree T of given DFA'''

        unchecked = []
        checked = []
        tree = Node(self.dfa.start)

        for trans in self.dfa.alphabet:
            child = self.dfa.delta(tree.stat, trans)
            if child == "sink":
                continue
            unchecked.append(child)
            tree.add_child(Node(child))
        
        for leaf in tree.children:
            self.construct_T_rec(self.dfa, leaf, unchecked, checked)

        return tree

    def construct_T_rec(self, dfa, node, unchecked, checked):
        if node.stat in checked:
            return
        else:
            for trans in dfa.alphabet:
                child = dfa.delta(node.stat, trans)
                if child == "sink":
                    continue
                if child not in checked:
                    unchecked.append(child)
                    node.add_child(Node(child))

            for leaf in node.children:
                self.construct_T_rec(dfa, leaf, unchecked, checked)

class Node(object):
    def __init__(self, stat):
        self.stat = stat
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)



if __name__ == '__main__':
