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


