#! /usr/bin/env python3

import unittest
from DFA.DFA import DFA 
import dfa_parser as DFAParser
import characteristic_set_teacher as csteacher
from learner import Learner



class TestCharacteristicSetTeacher(unittest.TestCase):
     def test_one(self):
        dfa = DFAParser.from_dict(
        {'accepts': {2, 0},
        'start': 0,
        'transitions': {0: {'a': 1, 'b': 2}, 1: {'a': 2}, 2: {'a': 0, 'b': 1}}})

        t = csteacher.CharacteristicSetTeacher(dfa)
        samples = t.construct_char_set()

        l = Learner(drawsteps=True)
        l.rpni(samples[0], samples[1])