#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler
import json
import urllib

def to_json(nombre, fich):
    f_json = nombre[:-4] + "json"
    json.dump(fich, open(f_json  , 'w'))
    return f_json

if __name__ == '__main__':

    parser = make_parser()
    fhandler = SmallSMILHandler()
    parser.setContentHandler(fhandler)

    
    try:
        fichero = sys.argv[1]
    except IndexError:
        sys.exit('Usage: python3 karaoke.py file.smil.')

    parser.parse(open(fichero))
        
    etiqs = fhandler.lista_etiqs # Guardamos la lista para trabajar con ella
    
    for line in etiqs:
        exit = line['etiqueta']
        #print(line)        
        for attr in line:
            if attr == 'etiqueta':
                exit = exit
            else:
                if not line[attr] == '':
                    exit = exit + '\t' + attr + '="' + line[attr] + '"'
       # exit = exit + '\n'
        print(exit)

    to_json(fichero, etiqs)

    print('---------------')
    print('')

    for line in etiqs:
        print(line)
        for attr in line:
                   
            if attr == 'src' and line[attr][:4] == 'http':
                local = line[attr].split('/')[-1]
                print(local)
                urllib.request.urlretrieve(line[attr], local)
                line[attr] = local
    
    
    
    
        
    
    
    
        
