#! /usr/bin/env python3

import unittest
from DFA.DFA import DFA
import dfa_parser as DFAParser
from learner import Learner
import characteristic_set_teacher as csteacher
import dfa_grapher as dfg
class TestCharacteristicSetTeacher(unittest.TestCase):
    def test_one(self):
        dfa = DFAParser.from_dict(
            {'accepts': {2, 0},
             'start': 0,
             'transitions': {0: {'a': 1, 'b': 2}, 1: {'a': 2}, 2: {'a': 0, 'b': 1}}})

        t = csteacher.CharacteristicSetTeacher(dfa)
        samples = t.construct_char_set()

        l = Learner(drawsteps=False)
        learned_dfa = l.rpni(samples[0], samples[1])
        for pos_sample in samples[0]:
            self.assertTrue(learned_dfa.recognizes(pos_sample))

        for neg_sample in samples[1]:
            self.assertFalse(learned_dfa.recognizes(neg_sample))


    def test_two(self):
        dfa = DFAParser.from_dict(
            {'accepts': {1},
             'start': 0,
             'transitions': {0: {'a': 0, 'b': 1}, 1: {'a': 1, 'b':2}, 2: {'a': 2, 'b': 0}}})

        t = csteacher.CharacteristicSetTeacher(dfa)
        samples = t.construct_char_set()

        l = Learner(drawsteps=False)
        learned_dfa = l.rpni(samples[0], samples[1])
        for pos_sample in samples[0]:
            self.assertTrue(learned_dfa.recognizes(pos_sample))

        for neg_sample in samples[1]:
            self.assertFalse(learned_dfa.recognizes(neg_sample))

    def test_single_node(self):
        dfa = DFAParser.from_dict(
            {'accepts': {0},
             'start': 0,
             'transitions': {0: {}}})

        t = csteacher.CharacteristicSetTeacher(dfa)
        samples = t.construct_char_set()

        l = Learner(drawsteps=False)
        learned_dfa = l.rpni(samples[0], samples[1])
        for pos_sample in samples[0]:
            self.assertTrue(learned_dfa.recognizes(pos_sample))

        for neg_sample in samples[1]:
            self.assertFalse(learned_dfa.recognizes(neg_sample))

    def test_one_transistion(self):
        dfa = DFAParser.from_dict(
            {'accepts': {1},
             'start': 0,
             'transitions': {0: {'a': 1}, 1: {'a': 2}, 2: {'a': 3}}})

        t = csteacher.CharacteristicSetTeacher(dfa)
        samples = t.construct_char_set()

        l = Learner(drawsteps=False)
        learned_dfa = l.rpni(samples[0], samples[1])
        for pos_sample in samples[0]:
            self.assertTrue(learned_dfa.recognizes(pos_sample))

        for neg_sample in samples[1]:
            self.assertFalse(learned_dfa.recognizes(neg_sample))

    def test_two_circular(self):
        dfa = DFAParser.from_dict(
            {'accepts': {0, 1},
             'start': 0,
             'transitions': {0: {'a': 1}, 1: {'a': 0}}})

        t = csteacher.CharacteristicSetTeacher(dfa)
        samples = t.construct_char_set()

        l = Learner(drawsteps=False)
        learned_dfa = l.rpni(samples[0], samples[1])
        for pos_sample in samples[0]:
            self.assertTrue(learned_dfa.recognizes(pos_sample))

        for neg_sample in samples[1]:
            self.assertFalse(learned_dfa.recognizes(neg_sample))



    def test_big_dfa(self):
        dfa = DFAParser.from_dict(
            {'accepts': {'aa','aaa','aaab','aba','b','babab' },    
             'start': 'start',
             'transitions': {'a': {'a': 'aa', 'b': 'ab'}, 'aa': {'a': 'aaa'}, 'aaa': {'b': 'aaab'}, 'aaab':{}, 'ab':{'a':'aba'}, 'aba': {}, 'b' : {'a': 'ba'}, 'ba': {'b': 'bab'}, 'bab': {'a': 'baba'}, 'baba': {'b': 'babab'}, 'babab': {}, 'sink': {}, 'start': {'a': 'a', 'b': 'b'}}})

        t = csteacher.CharacteristicSetTeacher(dfa)
        samples = t.construct_char_set()
      
        l = Learner(drawsteps=False)
        learned_dfa = l.rpni(samples[0], samples[1])
        
        for pos_sample in samples[0]:
            self.assertTrue(learned_dfa.recognizes(pos_sample))

        for neg_sample in samples[1]:
            self.assertFalse(learned_dfa.recognizes(neg_sample))



if __name__ == '__main__':
    unittest.main()





