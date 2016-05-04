#!/usr/bin/python3

"""
Cour de Cassation refiner for the Legifrance project.
Site: https://www.legifrance.gouv.fr
Details: Cour de Cassaion project
"""

from itertools import groupby
import re
import json


# Regular expressions for Cour de Cassation texts parsing
START_RE = re.compile(r"^\s*LA COUR DE CASSATION, (?P<civil> [^,]+), a rendu l'arrêt suivant :")
TITLE_RE = re.compile(r"""
        Cour\ de\ cassation,
        \ (?P<type>\S+),
        \ (?P<chamber>[\S ]+),
        \ (?P<date>[\S ]+),
        \ (?P<id>[0-9\-\.]+),
        """,
        re.VERBOSE
)
MOYEN_RE = re.compile(r"^\s*Sur le .*? moyen (unique)?")
ATTENDU_RE = re.compile(r"^\s*Attendu")
MOTIFS_RE = re.compile(r"^\s*(PAR CES MOTIFS|Par ces motifs)")
RESULT_RE_TYPES = [
    (re.compile(r"^\s*CASSE (ET|et) ANNULE"), "annul"),
    (re.compile(r"^\s*REJETTE le(s?) pourvoi(s?)"), "reject"),
    (re.compile(r"^\s*D(É|E)CLARE( le pourvoi)? IRRECEVABLE"), "unreceivable"),
    (re.compile(r"^\s*(DIT n'y avoir lieu|DIT N'Y AVOIR LIEU)"), "no_reason")
]
ARTICLES_RE_LIST = [
    re.compile(r"Vu l'article (?P<number>.+?) du (?P<codex>code .+)\,"),
    re.compile(r"Vu les articles (?:.+) du (?:code .+)( et (?:.+) du (?:code .+))+")
]

STATES = {
    'start': 0,
    'title_found': 1,
    'president_found': 2,
    'advocates_found': 3,
    'in_main_text': 4,
    'conclusion': 5,
    'remarks': 6,
}


def parse_text_list(tlist):
    """
    Parse and extract pure information from the line-splitted text list.
    """
    state = STATES['start']
    result = {}
    if len(tlist) <= 1:
        return {}
    parsed_title = TITLE_RE.match(tlist[1])
    if not parsed_title:
        return None
    result = {
        name: parsed_title.group(name)
        for name in ['type', 'chamber', 'date', 'id']
    }
    result['result'] = tlist[3]
    result['president'] = tlist[4][: tlist[4].find('(') - 1]
    result['advocates'] = tlist[5].split(', ')[: -1]
    return result


def sift(raw_text):
    result = []
    texts_list = [line.strip('\n') for line in raw_text.split('\n')]
    for k, g in groupby(texts_list, lambda l: l == '-'*80):
        if k == True:
            continue
        try:
            result.append(parse_text_list(list(g)))
        except ValueError:
            continue
    return result
