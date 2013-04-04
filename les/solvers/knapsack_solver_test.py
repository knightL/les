#!/usr/bin/env python
#
# -*- coding: utf-8; -*-
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

import unittest

from les.solvers import knapsack_solver

class Knapsack01SolverTest(unittest.TestCase):

  def test_solve(self):
    v = [8, 11, 6, 4]
    w = [5,  7, 4, 3]
    W = 14
    solution = [0.0, 1.0, 1.0, 1.0]
    value = 21.0
    problem = knapsack_solver.KnapsackProblem(v, w, W)
    solver = knapsack_solver.Knapsack01Solver()
    solver.load_problem(problem)
    solver.solve()
    self.assertEqual(value, solver.get_obj_value())
    for i in range(len(v)):
      self.assertEqual(solution[i], solver.get_col_solution()[i])

class FractionalKnapsackSolverTest(unittest.TestCase):

  def test_solve1(self):
    problem = knapsack_solver.KnapsackProblem([8, 11, 6, 4], [5,  7, 4, 3], 14)
    solver = knapsack_solver.FractionalKnapsackSolver()
    solver.load_problem(problem)
    solver.solve()
    self.assertEqual(22., solver.get_obj_value())
    self.assertEqual([1.0, 1.0, 0.5, 0.0], solver.get_col_solution())

  def test_solve2(self):
    problem = knapsack_solver.KnapsackProblem([50, 140, 60, 60], [5, 20, 10, 12],
                                              30)
    solver = knapsack_solver.FractionalKnapsackSolver()
    solver.load_problem(problem)
    solver.solve()
    self.assertEqual(220., solver.get_obj_value())
    self.assertEqual([1., 1., 0.5, 0.], solver.get_col_solution())

if __name__ == '__main__':
  unittest.main()
