#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):
    '''Clase para extraer la información relevante del fichero XML'''
    
    def __init__ (self):
        self.rlayout = ''
        self.region = ''
        self.img = ''
        self.audio = ''
        self.textstream = ''
        self.atributos_rlayout = ['width', 'height', 'background-color']
        self.atributos_region = ['id', 'top', 'bottom', 'left', 'right']
    
    def startElement(self, name, attrs):
        '''Método empleado al abrir una etiqueta'''
        if name == 'root-layout':
            for atributo in self.atributos_rlayout:
                self.rlayout = attrs.get(atributo, '')
                print(self.rlayout)
        
        if name == 'region':
            for atributo in self.atributos_region:
                self.region = attrs.get(atributo, '')
                print(self.region)
        
    def contenido(self, name, attrs):
        '''Método empleado para extraer la información relevante'''
        
        
if __name__ == '__main__':

    parser = make_parser()
    shandler = SmallSMILHandler()
    parser.setContentHandler(shandler)
    parser.parse(open('karaoke.smil'))
    
    
    
