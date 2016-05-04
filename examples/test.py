#!/usr/bin/python3

import sys
sys.path.append('../')

from gorynych import core_steps, ne_steps, sentiment_steps
import nltk


if __name__ == '__main__':
    text = ''
    with open('example-1.txt', 'r') as f:
        text = f.read()
    tokens = core_steps.tokenize(text)
    tags = core_steps.tagify(tokens)
    named_entities = ne_steps.get_named_entities(tags)
    sentiment = sentiment_steps.sentiment_bag_of_words(tokens)
    print(named_entities)
    print(sentiment)
    
