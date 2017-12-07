#! /usr/bin/env python3

import unittest
from DFA.DFA import DFA 
import dfa_parser as DFAParser
import characteristic_set_teacher as csteacher

class TestCharacteristicSetTeacher(unittest.TestCase):


    def test_one_node(self):
        dfa = DFAParser.from_dict(
        {'accepts': {0},
        'start': 0,
        'transitions': {0: {'a': 0}}})

        teacher = csteacher.CharacteristicSetTeacher(dfa)
        result = teacher.construct_char_set()
        self.assertCountEqual(result[0], ['a'])
        self.assertCountEqual(result[1], []) 

    def test_single_path(self):
        dfa = DFAParser.from_dict(
        {'accepts': {3},
        'start': 0,
        'transitions': {0: {'a': 1}, 1: {'a': 2}, 2: {'b': 3}}})

        teacher = csteacher.CharacteristicSetTeacher(dfa)
        result = teacher.construct_char_set()
        self.assertCountEqual(result[0], ['aab'])
        self.assertCountEqual(result[1], ['a', 'aa'])
        

    def test_simple_dfa(self):
        dfa = DFAParser.from_dict(
        {'accepts': {2},
        'start': 0,
        'transitions': {0: {'a': 1}, 1: {'a': 0, 'b': 2}, 2: {'a': 2, 'b': 0}}})

        teacher = csteacher.CharacteristicSetTeacher(dfa)
        result = teacher.construct_char_set()
        self.assertCountEqual(result[0], ['ab', 'aba'])
        self.assertCountEqual(result[1], ['a', 'abb', 'aa'])


if __name__ == '__main__':
    unittest.main()