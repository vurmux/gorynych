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


def get_lawsuit_urls(page_number):
    """
    Get all lawsuit URLs from the current search query page.
    """
    index = '/rechJuriJudi.do?reprise=true&champJuridictions=cour+de+cassation'
    page_parameter = '&page=' + str(page_number)
    index_url = ROOT_URL + index + page_parameter
    response = requests.get(index_url)
    soup = bs4.BeautifulSoup(response.text, "lxml")
    return [
        a.attrs.get('href')
        for a in soup.select('#center a[href^=\"/affichJuriJudi.do]')
    ]

def scrape(**parameters):
    """
    Entry point of spider module.
    Parameters:
    page_number - number of scraping page
    """
    urls = get_lawsuit_urls(parameters['page_number'])
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

if __name__ == '__main__':
    for page in scrape(page_number=1):
        print(page.encode('utf-8'))
