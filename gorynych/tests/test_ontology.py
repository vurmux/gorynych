#!/usr/bin/python3

import pytest
import networkx as nx

import gorynych

import gorynych.typesystem.nodes.basic.agent as agent
import gorynych.typesystem.nodes.basic.person as person
import gorynych.typesystem.edge as edge
import gorynych.typesystem.ontology as ontology

import gorynych.typesystem.gorynych_ontology


def test_ontology():
    a = agent.Agent(1)
    print(a)
    b = person.Person({"nationality": "RU"})
    print(dir(b))
    print(b.attributes)

    A = agent.Agent
    P = person.Person
    E = edge.Edge
    ont = ontology.Ontology(
        [P],
        [E],
        []
    )
    G = nx.MultiDiGraph()
    G.add_node(a)
    G.add_node(b)
    try:
        ont.check_graph_fit(G)
    except ValueError as e:
        print(e)

    G = gorynych.typesystem.gorynych_ontology.GORYNYCH_ONTOLOGY

    print(G)
    print(G.node_types)