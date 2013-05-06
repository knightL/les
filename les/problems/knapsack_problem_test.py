#!/usr/bin/env python
#
# Copyright (c) 2012-2013 Oleksandr Sviridenko
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from les.problems.knapsack_problem import KnapsackProblem
from les.problems.bilp_problem import BILPProblem
from les.utils import unittest

class KnapsackProblemTest(unittest.TestCase):

  def test_read_from_bilpp(self):
    bilp_problem = BILPProblem.build_from_scratch(
      [8, 2, 5, 5, 8, 3, 9, 7, 6],
      [[2., 3., 4., 1., 0., 0., 0., 0., 0.],
       [1., 2., 3., 2., 0., 0., 0., 0., 0.],
       [0., 0., 1., 4., 3., 4., 2., 0., 0.],
       [0., 0., 2., 1., 1., 2., 5., 0., 0.],
       [0., 0., 0., 0., 0., 0., 2., 1., 2.],
       [0., 0., 0., 0., 0., 0., 3., 4., 1.]],
      ['L'] * 6,
      [7, 6, 9, 7, 3, 5])
    knapsack_problem = KnapsackProblem("MY_PROBLEM", bilp_problem)
    self.assertEqual([8, 2, 5, 5, 8, 3, 9, 7, 6], knapsack_problem.get_values())
    self.assertEqual([3., 5., 10., 8., 4., 6., 12., 5., 3.], knapsack_problem.get_weights())
    self.assertEqual(37., knapsack_problem.get_max_weight())

if __name__ == '__main__':
  unittest.main()