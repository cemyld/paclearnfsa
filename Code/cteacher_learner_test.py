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
if __name__ == '__main__':
    unittest.main()

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
if __name__ == '__main__':
    unittest.main()

    def test_three(self):
        dfa = DFAParser.from_dict(
            {'accepts': {2,3,5},
             'start': 0,
             'transitions': {0: {'a': 1, 'b': 2}, 1: {'a': 3}, 3: {'a': 4}, 4: {'a': 5}}})

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

def test_four(self):
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

def test_five(self):
        dfa = DFAParser.from_dict(
            {'accepts': {'A'},
             'start': 'A',
             'transitions': {'A': {'a': 'B', 'b': 'A'}, 'B': {'a': 'A', 'b':'B'}}})

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

def test_six(self):
        dfa = DFAParser.from_dict(
            {'accepts': {'K'},
             'start': 'K',
             'transition':{ 'K': {'a': 'L', 'b': 'M'}, 'L': {'a': 'M', 'b': 'K'}, 'M': {'a': 'M', 'b': 'M'}}})

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

    def test_seven(self):
        dfa = DFAParser.from_dict(
            {'accepts': {'O'},
             'start': 'N',
             'transitions':{ 'N': {'a': 'O', 'b': 'P'}, 'O': {'a': 'P', 'b': 'N'}, 'P': {'a': 'P', 'b': 'P'}}})

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


    def test_eight(self):
        dfa = DFAParser.from_dict(
            {'accepts': {'Q','S'},
             'start': 'Q',
             'transitions':{ 'Q': {'a': 'R', 'b': 'T'}, 'R': {'a': 'T', 'b': 'S'}, 'S': {'a': 'R', 'b': 'U'}, 'T': {'a': 'T', 'b': 'T'}, 'U': {'a': 'T', 'b': 'T'}}})

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


    def test_nine(self):
        dfa = DFAParser.from_dict(
            {'accepts': {'V','X'},
             'start': 'X',
             'transitions':{ 'V': {'a': 'Y', 'b': 'Z'}, 'W': {'a': 'Z', 'b': 'V'}, 'X': {'a': 'W', 'b': 'Z'}, 'Y': {'a': 'Z', 'b': 'X'}, 'Z': {'a': 'Z', 'b': 'Z'}}})

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





