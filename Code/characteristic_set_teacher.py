#! /usr/bin/env python3

import teacher as teacher
import dfa_parser as DFAParser


class CharacteristicSetTeacher(teacher.Teacher):

    def __init__(self, dfa):
        teacher.Teacher.__init__(self, dfa)
        
        self.char_set = self.construct_char_set()
        self.pos_example = self.char_set[0]
        self.neg_example = self.char_set[1]
        self.used_pos = []
        self.used_neg = []

        
    # generate |T(A)|
    def construct_char_set(self):
        '''Construct a characteristic set of the DFA'''

        tree = self.construct_tree()
        start_node = tree[-1] # the last in the list is the starting node
        degree = self.degree(start_node)
        TA = []
        self.all_paths(start_node, '', '', TA)
        
        TA = list(filter(None, TA))

        result = [[], []]
        for item in TA:
            if self.dfa.recognizes(item): # put positive example in first list
                result[0].append(item)
            else:
                result[1].append(item) # put negative example in first list

        return result

    def get_pos_example(self):
        ''' Overwrite teacher's get_pos_example, here you will only get examples from character sets '''

        if len(self.used_pos) == len(self.pos_example):
            self.used_pos = []

        for example in self.pos_example:
            if example not in self.used_pos:
                self.used_pos.append(example)
                return(example, '+')
        
    def get_neg_example(self):
        ''' Overwrite teacher's get_neg_example, here you will only get examples from character sets '''
  
        if len(self.used_neg) == len(self.pos_example):
            self.used_neg = []

        for example in self.neg_example:
            if example not in self.used_neg:
                self.used_neg.append(example)
                return(example, '-')
    
    def all_paths(self, start, string ,trans, char_set):
        '''Recursively traversal throught the tree'''
        string += trans
        if len(start.children) == 0:
            char_set.append(string)
            return

        for k, v in start.children.items():
            if string not in char_set:
                char_set.append(string)

            self.all_paths(v, string, k, char_set)

                
    def construct_tree(self):
        '''Construct a tree T(A) of given DFA'''

        checked = []
        unchecked = []
        node_list = []
        start = Node(self.dfa.start)
        unchecked.append(start.state)
        self.construct_tree_rec(start, checked, unchecked, node_list)
        return node_list 


    def construct_tree_rec(self, node, checked, unchecked, node_list):
        '''recursive constructing tree'''
        if len(unchecked) == 0:
            return

        unchecked.remove(node.state)
        checked.append(node.state)

        for alph in self.dfa.alphabet:
            child = self.dfa.delta(node.state, alph)
            if child == "sink":
                continue
            elif child in checked: # if children already check, don't go into it
                node.add_child(alph, Node(child))
            else:
                unchecked.append(child)
                node.add_child(alph, self.construct_tree_rec(Node(child), checked, unchecked, node_list))
                
        
        node_list.append(node)
        return node
    
    def degree(self, tree_node):
        '''Find the degree(depth) of the tree'''
        if len(tree_node.children) == 0:
            return 1

        children_depth = []
        
        for k, node in tree_node.children.items():
            children_depth.append(self.degree(node))

        return max(children_depth) + 1


class Node(object):
    '''Node class for the tree'''
    def __init__(self, state):
        self.state = state
        self.children = {} # children are stored like {transistion: Node(state)}

    def add_child(self, trans, obj):
        self.children[trans] = obj


def recursive_print_tree(node, trans='s', depth=0):
    '''Printing the tree in a more human readable form'''
    print('   ' * depth + trans + ': ' + str(node.state))
    for k, v in node.children.items():
        recursive_print_tree(v, k, depth+1)


if __name__ == '__main__':
    dfa = DFAParser.from_dict(
    {'accepts': {2},
    'start': 0,
    'transitions': {0: {'a': 1  , 'b': 1}, 1: {'a': 0, 'b': 2}, 2: {'a': 2, 'b': 0}}}
    )
    
    teacher = CharacteristicSetTeacher(dfa)
    tree = teacher.construct_tree()
    print("Degree: " + str(teacher.degree(tree[-1])))
    recursive_print_tree(tree[-1])

    print(teacher.char_set)
    for i in range(50):
        print(teacher.get_pos_example())
        print(teacher.get_neg_example())