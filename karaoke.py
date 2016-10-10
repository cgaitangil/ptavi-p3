#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler
import json
import urllib


class KaraokeLocal(SmallSMILHandler):

    def __init__(self, fichero):
        parser = make_parser()
        fhandler = SmallSMILHandler()
        parser.setContentHandler(fhandler)
        parser.parse(open(fichero))
        self.etiqs = fhandler.get_tags()

    def __str__(self):
        for line in self.etiqs:
            exit = line['etiqueta']
            for attr in line:
                if attr == 'etiqueta':
                    exit = exit
                else:
                    if not line[attr] == '':
                        exit = exit + '\t' + attr + '="' + line[attr] + '"'
            print(exit)

    def to_json(self, nombre):
        f_json = nombre[:-4] + "json"
        json.dump(self.etiqs, open(f_json, 'w'))
        return f_json

    def do_local(self):
        for line in self.etiqs:
            for attr in line:
                if attr == 'src' and line[attr][:4] == 'http':
                    local = line[attr].split('/')[-1]
                    urllib.request.urlretrieve(line[attr], local)
                    line[attr] = local

if __name__ == '__main__':

    try:
        fichero = sys.argv[1]
    except IndexError:
        sys.exit('Usage: python3 karaoke.py file.smil.')

    objeto = KaraokeLocal(fichero)

    objeto.__str__()

    objeto.to_json(fichero)

    objeto.do_local()

    objeto.__str__()
