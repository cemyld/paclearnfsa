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
        self.assertCountEqual(result, ['a'])   

    def test_single_path(self):
        dfa = DFAParser.from_dict(
        {'accepts': {2},
        'start': 0,
        'transitions': {0: {'a': 1}, 1: {'a': 2}, 2: {'b': 3}}})

        teacher = csteacher.CharacteristicSetTeacher(dfa)
        result = teacher.construct_char_set()
        self.assertCountEqual(result, ['a', 'aa', 'aab'])


    def test_simple_dfa(self):
        dfa = DFAParser.from_dict(
        {'accepts': {2},
        'start': 0,
        'transitions': {0: {'a': 1}, 1: {'a': 0, 'b': 2}, 2: {'a': 2, 'b': 0}}})

        teacher = csteacher.CharacteristicSetTeacher(dfa)
        result = teacher.construct_char_set()
        self.assertCountEqual(result, ['a', 'ab', 'abb', 'aba', 'aa'])




if __name__ == '__main__':
    unittest.main()