#!/usr/bin/python3

import nltk
from nltk import ne_chunk
from nltk.tree import Tree


def chop_ne_chunks(tagged_tokens):
    return ne_chunk(tagged_tokens)


def get_raw_named_entities(ne_chunks):
    prev = None
    raw_named_entities = set([])
    current_chunk = []
    current_label = ''
    for chunk in ne_chunks:
        if type(chunk) == Tree:
            current_chunk.append(
                " ".join([
                    token
                    for token, pos in chunk.leaves()
                ])
            )
            current_label = chunk.label()
        elif current_chunk:
            named_entity = (" ".join(current_chunk))
            if named_entity not in raw_named_entities:
                raw_named_entities.add((named_entity, current_label))
                current_chunk = []
                current_label = ''
    result = (
        'raw_named_entities',
        raw_named_entities
    )
    return result


def refine_named_entities(raw_named_entities):
    in_label, named_entities = raw_named_entities
    if in_label != 'raw_named_entities':
        raise ValueError
    ne_set = set([elem[0] for elem in named_entities])
    to_delete = set([])
    for element in named_entities:
        entity, label = element
        for cutting_postfix in ['n', 's', '\'s']:
            cut_entity = __cut_entity_end(entity, cutting_postfix)
            if cut_entity and cut_entity in ne_set:
                to_delete.add(element)
    result = (
        'refined_named_entities',
        named_entities - to_delete
    )
    return result


def __cut_entity_end(entity_string, end_string):
    length = len(end_string)
    if entity_string[-1 * length:] == end_string:
        return entity_string[: -1 * length]
    else:
        return False
