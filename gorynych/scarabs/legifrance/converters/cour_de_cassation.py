#!/usr/bin/python3

"""
Cour de Cassation refiner for the Legifrance project.
Site: https://www.legifrance.gouv.fr
Details: Cour de Cassaion project
"""


def convert_to_orientdb(obj):
    result = ''
    try:
        result += (
            'CREATE VERTEX Lawsuit '
            'CONTENT {"id": "' + str(obj['id']) +
            '", "result": "' + str(obj['result']) +
            '", "date": "' + str(obj['date']) +
            '", "type": "' + str(obj['type']) + '"}\n'
        )
        result += ('CREATE VERTEX Chamber '
                'CONTENT {"name": "' + obj['chamber'] + '"}'
                '\n'
        )
        result += ('CREATE VERTEX Judge '
                'CONTENT {"name": "' + obj['president'] + '"}'
                '\n'
        )
        for advocate in obj['advocates']:
            result += ('CREATE VERTEX Advocate '
                    'CONTENT {"name": "' + advocate + '"}'
                    '\n'
            )
        result += ('CREATE EDGE '
                'FROM (SELECT FROM Chamber WHERE name = "' + obj['chamber'] + '") '
                'TO (SELECT FROM Lawsuit WHERE id = "' + obj['id'] + '")'
                '\n'
        )
        result += ('CREATE EDGE '
                'FROM (SELECT FROM Judge WHERE name = "' + obj['president'] + '") '
                'TO (SELECT FROM Lawsuit WHERE id = "' + obj['id'] + '")'
                '\n'
        )
        for advocate in obj['advocates']:
            result += ('CREATE EDGE '
                    'FROM (SELECT FROM Advocate WHERE name = "' + advocate + '") '
                    'TO (SELECT FROM Lawsuit WHERE id = "' + obj['id'] + '")'
                    '\n'
            )
    except (KeyError, TypeError):
        return None
    return result
