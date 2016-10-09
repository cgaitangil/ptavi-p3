#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler

if __name__ == '__main__':

    parser = make_parser()
    fhandler = SmallSMILHandler()
    parser.setContentHandler(fhandler)
    try:
        parser.parse(open(sys.argv[1]))
    except IndexError:
        sys.exit('Expected File')
        
    etiqs = fhandler.lista_etiqs # Guardamos la lista para trabajar con ella
    
    print(etiqs)
    print('')
    
    for line in etiqs:
        exit = line['etiqueta']
        print(line)        
        for attr in line:
            if attr == 'etiqueta':
                exit = exit
            else:
                if not line[attr] == '':
                    exit = exit + ',' + attr + '="' + line[attr] + '"'
        exit = exit + '\n'
        print(exit)
        
        print('')
    
    
    
        
