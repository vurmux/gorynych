#!/usr/bin/python3

from pprint import pprint
import re
import sys
sys.path.append('../')

from gorynych.engines.nltk import core_steps, ne_steps, sentiment_steps
import nltk
import json
import time


def find_patterns(ne_chunks):
    for i in range(len(ne_chunks) - 4):
        try:
            if (ne_chunks[i].label() == 'PERSON' and
                    ne_chunks[i+1][1] == 'IN' and
                    (ne_chunks[i+2].label() == 'GPE' or
                     ne_chunks[i+2].label() == 'ORGANIZATION')):
                print(ne_chunks[i: i+4])
        except:
            pass


OF = re.compile(r'.*\bof\b.*\bthe\b.*')

if __name__ == '__main__':
    start_time = time.time()
    tweets = []
    has_ne = 0
    has_no_ne = 0
    with open('tweets.json') as f:
        tweets = [json.loads(l) for l in f.readlines()]
    for t in tweets:
        if 'text' not in t:
            continue
        text = t['text'].lower()
        print(text.encode('utf-8'))
        tokens = core_steps.tokenize(text)
        tags = core_steps.tagify(tokens)
        ne_chunks = ne_steps.chop_ne_chunks(tags)
        named_entities = ne_steps.get_raw_named_entities(ne_chunks)
        sentiment = sentiment_steps.sentiment_bag_of_words(tokens)
        refined_named_entities = ne_steps.refine_named_entities(named_entities)
        if named_entities[1]:
            print(
                str(named_entities[1]).encode('utf-8'),
                '|',
                str(sentiment[1]).encode('utf-8'),
            )
            has_ne += 1
        else:
            has_no_ne += 1
    end_time = time.time()
    calc_time = end_time - start_time
    print()
    print()
    print(str(float(has_ne)/len(tweets)*100) + '% of tweets has NE\'s')
    print(
        'Whole calc time - {0} seconds ({1} tweets)\nTime for 1 tweet - {2} seconds'.format(
            str(int(calc_time)),
            str(len(tweets)),
            str(float(calc_time)/len(tweets))
        )
    )
