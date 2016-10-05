#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Cour de Cassation lawsuits spider for the Legifrance project.
Site: https://www.legifrance.gouv.fr
Details: Cour de Cassaion project
"""

import requests
import bs4
import re
import codecs
from itertools import groupby
import json


BR = re.compile(r'<br/>(\\n<br/>)+')
SPACE_RE = re.compile(r'\s+')
ADVOCATES_RE = re.compile(
    r'''
        sident</strong>\s*
        (\s*<.+?>\s*)*
        (?P<advocates> .*?avocat\(s\))
        (\s*<.+?>\s*)+
        Texte
    ''',
    re.VERBOSE
)

ROOT_URL = 'https://www.legifrance.gouv.fr'

# Regular expressions for Cour de Cassation texts parsing
START_RE = re.compile(
    r"^\s*LA COUR DE CASSATION, (?P<civil> [^,]+), a rendu l'arrêt suivant :"
)
TITLE_RE = re.compile(
    r"""
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
    re.compile(
        r"Vu les articles (?:.+) du (?:code .+)( et (?:.+) du (?:code .+))+"
    )
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


class LegifranceCassationScarab(object):

    def __init__(self):
        self.uid = str(self.__hash__())
        self.name = "LegifranceCassationScarab"

    def run(self, **parameters):
        """
        Entry point of scarab module.
        Parameters:
        page_number - number of scraping page
        """
        for page in self.scrape(parameters['page_number']):
            yield self.sift(page)

    def run_default(self):
        """
        Entry point of scarab module with default configuration.
        """
        for page in self.scrape(page_number=1):
            yield self.sift(page)

    def scrape(self, **parameters):
        urls = self._get_lawsuit_urls(parameters['page_number'])
        for i in urls:
            url = ROOT_URL + i
            response = requests.get(url)
            soup = bs4.BeautifulSoup(response.text.encode('utf-8'), "lxml")
            result = ""
            for j in soup.select('strong'):
                result += SPACE_RE.sub(' ', j.get_text().strip()) + '\n'
            advocates = ADVOCATES_RE.search(str(soup))
            if advocates:
                result += advocates.group('advocates') + '\n'
            result += '\n'
            for j in soup.select('contenu'):
                result += j.get_text() + '\n'
            result += "-"*80 + '\n'
            yield result

    def sift(self, raw_text):
        result = []
        texts_list = [line.strip('\n') for line in raw_text.split('\n')]
        for k, g in groupby(texts_list, lambda l: l == '-'*80):
            if k:
                continue
            try:
                result.append(self._parse_text_list(list(g)))
            except ValueError:
                continue
        return result

    def _parse_text_list(self, tlist):
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

    def _get_lawsuit_urls(self, page_number):
        """
        Get all lawsuit URLs from the current search query page.
        """
        index = '/rechJuriJudi.do?reprise=true&' + \
                'champJuridictions=cour+de+cassation'
        page_parameter = '&page=' + str(page_number)
        index_url = ROOT_URL + index + page_parameter
        response = requests.get(index_url)
        soup = bs4.BeautifulSoup(response.text, "lxml")
        return [
            a.attrs.get('href')
            for a in soup.select('#center a[href^=\"/affichJuriJudi.do]')
        ]


if __name__ == '__main__':
    scarab = LegifranceCassationScarab()
    for elem in scarab.run_default():
        print(str(elem).encode('utf-8'))
