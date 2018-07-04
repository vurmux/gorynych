import networkx as nx

class Ontology(object):
    """Class for ontology"""
    def __init__(self, node_types=[], edge_types=[], relations=[]):
        self.node_types = {
            elem.meta['typename']: elem
            for elem in node_types
        }
        self.edge_types = {
            elem.meta['typename']: elem
            for elem in edge_types
        }
        self.relations = relations

    def check_graph_fit(self, graph, ignore=False):
        # Check an existense of all node types in ontology
        for node in graph.nodes:
            if node.meta['typename'] not in self.node_types and ignore == False:
                raise ValueError("Node type is not found in the current ontology: {}".format(
                    node.meta['typename']
                ))
        return True

    def fit_graph(self, G):
        pass

    def _validate_self(self):
        pass

    def _validate_graph(self):
        pass