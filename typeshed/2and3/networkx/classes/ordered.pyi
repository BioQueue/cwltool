# Stubs for networkx.classes.ordered (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .digraph import DiGraph
from .graph import Graph
from .multidigraph import MultiDiGraph
from .multigraph import MultiGraph
from typing import Any

class OrderedGraph(Graph):
    node_dict_factory: Any = ...
    adjlist_outer_dict_factory: Any = ...
    adjlist_inner_dict_factory: Any = ...
    edge_attr_dict_factory: Any = ...
    def fresh_copy(self): ...

class OrderedDiGraph(DiGraph):
    node_dict_factory: Any = ...
    adjlist_outer_dict_factory: Any = ...
    adjlist_inner_dict_factory: Any = ...
    edge_attr_dict_factory: Any = ...
    def fresh_copy(self): ...

class OrderedMultiGraph(MultiGraph):
    node_dict_factory: Any = ...
    adjlist_outer_dict_factory: Any = ...
    adjlist_inner_dict_factory: Any = ...
    edge_key_dict_factory: Any = ...
    edge_attr_dict_factory: Any = ...
    def fresh_copy(self): ...

class OrderedMultiDiGraph(MultiDiGraph):
    node_dict_factory: Any = ...
    adjlist_outer_dict_factory: Any = ...
    adjlist_inner_dict_factory: Any = ...
    edge_key_dict_factory: Any = ...
    edge_attr_dict_factory: Any = ...
    def fresh_copy(self): ...
