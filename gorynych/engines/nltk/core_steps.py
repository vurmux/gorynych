#!/usr/bin/python3

from itertools import groupby
import nltk
from nltk import pos_tag, word_tokenize, sent_tokenize


def sentence_split(raw_text):
    return sent_tokenize(raw_text)


def tokenize(raw_text):
    return word_tokenize(raw_text)


def tagify(tokens):
    return pos_tag(tokens)


def tagged_sentence_split(tagged_tokens):
    # tagged_sentences_tokens
    return [list(g) for k, g in groupby(tagged_tokens, lambda x: x != ('.', '.')) if k]
