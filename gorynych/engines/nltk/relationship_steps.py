#!/usr/bin/python3

import os
import nltk
import re
import json
import gorynych


with open(
        os.path.join(
            gorynych.__path__[0],
            'dicts',
            'relations.json'
        ),
        'r'
) as r:
    RELATIONS = json.loads(r.read())
for rel_type in RELATIONS:
    rel_type['regexp'] = re.compile(rel_type['regexp'])


def get_raw_relstrings(ne_chunks):
    semi_rel = nltk.sem.relextract.semi_rel2reldict(
        nltk.sem.relextract.tree2semi_rel(ne_chunks)
    )
    result = []
    for rel in semi_rel:
        for rel_type in RELATIONS:
            if (rel['objclass'] not in rel_type['objclass'] or
                    rel['subjclass'] not in rel_type['subjclass']):
                continue
            match = rel_type['regexp'].match(rel['untagged_filler'])
            if match and match.end() == len(rel['untagged_filler']):
                result.append(rel)
    return result
