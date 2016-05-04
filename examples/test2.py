#!/usr/bin/python3

import sys
from pprint import pprint
sys.path.append('../')
import re
IN_THE = re.compile('\\s(in)(\\sthe)?\\s')

from gorynych import core_steps, ne_steps, sentiment_steps, relationship_steps
import nltk


if __name__ == '__main__':
    for i in range(100):
        text = nltk.corpus.reuters.open(nltk.corpus.reuters.fileids()[i]).read()
        tokens = core_steps.tokenize(text)
        tags = core_steps.tagify(tokens)
        chunks = ne_steps.chop_ne_chunks(tags)
        sentences = core_steps.tagged_sentence_split(tags)
        for s in sentences:
            s_chunks = ne_steps.chop_ne_chunks(s)
            s_ne = ne_steps.get_raw_named_entities(s_chunks)
            s_rne = ne_steps.refine_named_entities(s_ne)
            s_rel = relationship_steps.get_raw_relstrings(s_chunks)
            if s_rel != []:
                for r in s_rel:
                    print(r['subjsym'], r['untagged_filler'], r['objsym'])
        named_entities = ne_steps.get_raw_named_entities(chunks)
        refined_ne = ne_steps.refine_named_entities(named_entities)
        sentiment = sentiment_steps.sentiment_bag_of_words(tokens)
        relations = relationship_steps.get_raw_relstrings(chunks)
        print(relations)
        print(tags)
        print(named_entities)
        print(sentiment)
        print(relations)
        print(refined_ne)
        print(core_steps.tagged_sentence_split(tags))
        print()
    
