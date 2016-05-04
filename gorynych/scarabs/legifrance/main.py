#!/usr/bin/python3
# -*- coding: utf-8 -*-


import spiders.cour_de_cassation
import sifters.cour_de_cassation
import converters.cour_de_cassation


if __name__ == '__main__':
    for page in spiders.cour_de_cassation.scrape(page_number=1):
        sifted = sifters.cour_de_cassation.sift(page)
        orientdb_data = [converters.cour_de_cassation.convert_to_orientdb(s) for s in sifted]
        for query in orientdb_data:
            if query:
                print(query.encode('utf-8'))