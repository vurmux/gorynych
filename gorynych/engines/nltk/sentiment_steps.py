#!/usr/bin/python3

import nltk
from nltk import ne_chunk
from nltk.tree import Tree


POSITIVE_SET = set([
    line
    for line in nltk.data.load(
            'corpora/opinion_lexicon/positive-words.txt',
            'text').split('\n')
    if not line.startswith(';')
])

NEGATIVE_SET = set([
    line
    for line in nltk.data.load(
            'corpora/opinion_lexicon/negative-words.txt',
            'text').split('\n')
    if not line.startswith(';')
])


def sentiment_bag_of_words(tokens):
    bag = set(tokens)
    sentiment = {}
    pos_score = 0
    neg_score = 0
    for token in bag:
        if token in POSITIVE_SET:
            pos_score += 1
        if token in NEGATIVE_SET:
            neg_score += 1
    score = pos_score - neg_score
    polarity = int(((pos_score + neg_score) / (len(tokens))) * 100)
    sentiment['polarity'] = polarity
    result_score = __construct_percentage_score(score, len(tokens))
    sentiment['score'] = result_score
    if result_score == 0:
        sentiment_type = 'neutral'
    elif result_score > 0:
        sentiment_type = 'positive'
    elif result_score < 0:
        sentiment_type = 'negative'
    sentiment['type'] = sentiment_type
    result = ('sentiment', sentiment)
    return result


def __construct_percentage_score(score, length):
    abs_score = abs(score)
    if length <= 0:
        raise ValueError
    result_score = int((score / length) * 100)
    return result_score
