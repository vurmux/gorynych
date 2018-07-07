from collections import defaultdict
from itertools import groupby

import networkx as nx

class Graph(object):
    """
    """

    def __init__(self, ontology, graph):
        self.G = graph
        self.ontology = ontology
    
    @property
    def graph(self):
        return self.G

    @property
    def nodes(self):
        return self.G.nodes
    
    @property
    def edges(self):
        return self.G.edges
    
    @property
    def ontology(self):
        return self.ontology

    def merge(self, other):
        self_d = defaultdict(list)
        other_d = defaultdict(list)

        for node in self.G.nodes:
            self_d[node.meta['hierarchy']].append(node)
        for node in other.G.nodes:
            other_d[node.meta['hierarchy']].append(node)
        self_h = set(self_d.keys())
        other_h = set(other_d.keys())

        types_to_add = other_h - self_h
        both_types = self_h & other_h

        fused_nodes = [[], []]

        for type_h in types_to_add:
            for node in other_d[type_h]:
                self.G.add_node(node)
        for type_h in both_types:
            for other_node in other_d[type_h]:
                is_fused = False
                for self_node in self_d[type_h]:
                    # FIXME: Implement can_fuse method
                    # if self_node.can_fuse(other_node):
                    if self_node.attributes['name'] == other_node.attributes['name']:
                        self_node.fuse(other_node)
                        is_fused = True
                        fused_nodes[0].append(self_node)
                        fused_nodes[1].append(other_node)
                if not is_fused:
                    self.G.add_node(other_node)

        for edge in other.edges:
            #  HACK: This dirty code must be fixed
            if edge[0] in fused_nodes[1] and edge[1] not in fused_nodes[1]:
                i0 = fused_nodes[1].index(edge[0])
                self.G.add_edge(
                    fused_nodes[0][i0],
                    edge[1],
                    edge=other.edges[edge]['edge']
                )
            elif edge[0] not in fused_nodes[1] and edge[1] in fused_nodes[1]:
                i1 = fused_nodes[1].index(edge[1])
                self.G.add_edge(
                    edge[0],
                    fused_nodes[0][i1],
                    edge=other.edges[edge]['edge']
                )
            elif edge[0] in fused_nodes[1] and edge[1] in fused_nodes[1]:
                i0 = fused_nodes[1].index(edge[0])
                i1 = fused_nodes[1].index(edge[1])
                self.G.add_edge(
                    fused_nodes[0][i0],
                    fused_nodes[0][i1],
                    edge=other.edges[edge]['edge']
                )
            else:
                self.G.add_edge(edge)
        
        # Find and delete edge duplicates
        edges_to_delete = []
        for _, in_edges in groupby(list(G.edges), lambda x: x[0]):
            for _, in_out_edges in groupby(in_edges, lambda x: x[1]):
                for i, edge in enumerate(in_out_edges):
                    edges_to_check = list(in_out_edges)[:i+1]
                    for e in edges_to_check:
                        # FIXME: implement can_fuse()
                        if self.G.edges[edge]['edge'].meta['hierarchy'] == self.G.edges[e]['edge'].meta['hierarchy']:
                            self.G.edges[e]['edge'].fuse(self.G.edges[edge]['edge'])
                            edges_to_delete.append(edge)
                            break
        for edge in edges_to_delete:
            self.G.remove_edge(edge[0], edge[1], edge[2])