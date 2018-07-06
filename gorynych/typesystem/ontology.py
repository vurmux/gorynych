import networkx as nx

class Ontology(object):
    """Class for ontology"""

    meta = {
        "name": "",
        "author": '"",
        "short_description": "",
        "long_description": "",
        "tags": []
    }

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

    def get_node_type(self, typename):
        if typename in self.node_types:
            return self.node_types[typename]
        else:
            raise ValueError("Ontology has no node type: {}".format(typename))

    def get_edge_type(self, typename):
        if typename in self.edge_types:
            return self.edge_types[typename]
        else:
            raise ValueError("Ontology has no edge type: {}".format(typename))

    def _validate_self(self):
        pass

    def _validate_graph(self):
        pass