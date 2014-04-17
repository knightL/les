
import networkx

from les.mp_model import MPModel
from les.decomposers import decomposer_base
from les.graphs.decomposition_tree import DecompositionTree
from les.utils import logging

def _get_indices(m, i):
  start = m.indptr[i]
  size = m.indptr[i + 1] - start
  result = []
  for j in xrange(start, start + size):
    result.append(m.indices[j])
  return result


class FinkelsteinAdvDecomposer(decomposer_base.DecomposerBase):
  '''
  :param model: A :class:`~les.mp_model.mp_model.MPModel` based model instance.
  '''

  def __init__(self, model):
    decomposer_base.DecomposerBase.__init__(self, model)
    self._u = []
    self._s = []
    self._m = []
    self._p = []
    self._used = []
    self._used2 = []
    self._layers =[]
    self._layermodel =[]

  def get_component(self,i):
    if self._p[i]!=i:
        self._p[i]=self.get_component(self._p[i])
    return self._p[i]

  def unite_components(self, i, j):

    i=self.get_component(i)
    j=self.get_component(j)
    self._p[i]=j

  def decompose(self, initial_cols=[0], max_separator_size=0,
                merge_empty_blocks=True):
    '''Decomposes model into submodels starting by initial cols. By default
    starts from column 0. Default max separator size is 11.

    :param initial_cols: A list of integers.
    :param max_separator_size: An integer that represents max available
      separator size.
    :param merge_empty_blocks: ``True`` or ``False``, whether or not we need to
      merge empty blocks.
    '''
    if max_separator_size:
      raise NotImplementedError()
    logging.info('Decompose model %s', self._model.get_name())

    self._used=[]
    self._used2=[]
    self._p=[]

    m = self._model.get_rows_coefficients()

    j_to_i_mapping = {}
    for j in range(m.shape[1]):
      j_to_i_mapping[j] = set()

    # TODO(d2rk): use interaction graph?
    g = networkx.Graph()
    g.add_nodes_from(range(m.shape[1]))
    for i in xrange(m.shape[0]):
      J_ = _get_indices(m, i)
      for j in range(len(J_) - 1):
        j_to_i_mapping[J_[j]].add(i)
        for j_ in range(j + 1, len(J_)):
          g.add_edge(J_[j], J_[j_])
      j_to_i_mapping[J_[-1]].add(i)

    def get_neighbors(nodes):
      neighbors = set()
      for node in nodes:
        neighbors.update(g.neighbors(node))
      neighbors.update(nodes)
      return neighbors
      
    def U(m_):
      u_=set()
      for i in xrange(m.shape[0]):
        ok = True
        K_ = _get_indices(m, i)
        for j in K_:
          ok &= j in m_
        if ok:
          u_.add(i)
      return u_

    self._m = [set(initial_cols) | get_neighbors(set(initial_cols))]
    self._s = [set()]
    self._u = [set()]

    i = len(self._m)
    J = get_neighbors(self._m[i - 1])
    while True:
      M_ = J - self._m[i - 1] - self._s[i - 1]
      if not len(M_):
        break
      T = get_neighbors(M_)
      J_ = T - M_
      self._m.append(M_)
      self._u.append(set())
      self._s.append(J_ & J)
      self._m[i - 1] -= self._s[i]
      J = T
      i += 1
    
    for j in range(i):
      current= self._m[j] | self._s[j]
      if j+1 < i:
        current.update(self._s[j+1])
      self._u[j] = U(current)
    
    tree = DecompositionTree(self._model)
    
    for j in range(m.shape[1]):
      self._p.append(j)
      self._used.append(0)
      self._used2.append(0)
    
    self._layers=[]
    self._layermodel=[]
    for j in range(i):
      self._layers.append([])
      self._layermodel.append([])
    for j in range(i-1,-1,-1):
      current=self._m[j] | self._s[j]
      separator=set() | self._s[j]
      if j+1<i:
        current.update(self._s[j+1])
        separator.update(self._s[j+1])
      for k in current:
        self._used[k]=1
      for k in current - separator:
        T=get_neighbors([k])
        for _k in T:
          if self._used[_k]:
            self.unite_components(k,_k)
      for k in current:
        if not self._used2[k]:
          self._layers[j].append(set())
          for _k in current:
            if self.get_component(k)==self.get_component(_k):
              self._layers[j][-1].add(_k)
              self._used2[_k]=1
          u=U(self._layers[j][-1])
          self._layermodel[j].append(self._model.slice(u, self._layers[j][-1]))
          tree.add_node(self._layermodel[j][-1])
          if j!=i-1:
            for _k in range(len(self._layers[j+1])):
              if len( self._layers[j][-1] & self._layers[j+1][_k] )>0:
                tree.add_edge(self._layermodel[j][-1], self._layermodel[j+1][_k],
                    [self.get_model().get_columns_names()[i] for i in self._layers[j][-1] & self._layers[j+1][_k]])
      for k in separator:
        T=get_neighbors([k])
        for _k in T:
          if self._used[_k]:
            self.unite_components(k,_k)
    tree.set_root(self._layermodel[0][0])
          

    self._decomposition_tree = tree
