
from les.mp_model import MPModelBuilder
from les.decomposers import finkelstein_adv_decomposer
from les.utils import unittest


class FinkelsteinAdvDecomposerTest(unittest.TestCase):

  def test_decompose1(self):
    model = MPModelBuilder.build_from_scratch(
      [8, 2, 5, 5, 8, 3, 9, 7, 6],
      [[2, 3, 4, 1, 0, 0, 0, 0, 0],
       [1, 2, 3, 2, 0, 0, 0, 0, 0],
       [0, 0, 1, 4, 3, 4, 2, 0, 0],
       [0, 0, 2, 1, 1, 2, 5, 0, 0],
       [0, 0, 0, 0, 0, 0, 2, 1, 2],
       [0, 0, 0, 0, 0, 0, 3, 4, 1]],
      ['L'] * 6,
      [7, 6, 9, 7, 3, 5])
    decomposer = finkelstein_adv_decomposer.FinkelsteinAdvDecomposer(model)
    decomposer.decompose()
    
    layer = [[set([0,1,2,3])], [set([2,3,4,5,6])], [set([6,7,8])]]
    self.assert_equal(len(layer),len(decomposer._layers))
    for i in range(len(layer)):
      self.assert_equal(len(layer[i]),len(decomposer._layers[i]))
      for j in range(len(layer[i])):
        self.assert_equal(layer[i][j],decomposer._layers[i][j])
    
    tree = decomposer.get_decomposition_tree()
    
    p0=tree.node[tree.get_root()].get_model()
    self.assert_equal([u'x1',u'x2',u'x3',u'x4'],sorted(p0.get_columns_names()))
    p1=tree.node[tree.neighbors(tree.get_root())[0]].get_model()
    self.assert_equal([u'x3',u'x4',u'x5',u'x6',u'x7'],sorted(p1.get_columns_names()))


  def test_decompose2(self):
    model = MPModelBuilder.build_from_scratch(
      [1, 1, 1, 1, 1, 1, 1 ],
      [[1, 1, 1, 0, 0, 0, 0],
       [0, 1, 0, 1, 1, 0, 0],
       [0, 0, 1, 0, 0, 1, 1]],
      ['L'] * 3,
      [2, 2, 2])
    decomposer = finkelstein_adv_decomposer.FinkelsteinAdvDecomposer(model)
    decomposer.decompose()
    
    tree = decomposer.get_decomposition_tree()
    
    layer = [[set([0,1,2])], [set([1,3,4]), set([2,5,6])]]
    self.assert_equal(len(layer),len(decomposer._layers))
    for i in range(len(layer)):
      self.assert_equal(len(layer[i]),len(decomposer._layers[i]))
      for layers1, layers2 in ( (layer[i], decomposer._layers[i]) ,(decomposer._layers[i],layer[i]) ):
        for j in range(len(layers1)):
          ok=False
          for k in range(len(layers2)):
            if layers2[k]==layers1[j]:
              ok=True
          if not ok:
            print(layers1[j])
            print(layers2)
          self.assert_equal(ok,True)


if __name__ == '__main__':
  unittest.main()
