#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):
    '''Clase para extraer la información relevante del fichero XML'''
    
    def __init__ (self):
        
#Para iterar        self.etiquetas = ['root-layout', 'region', 'img', 'audio', 
#                          'textsstream']
        
        self.atributos_rlayout = ['width', 'height', 'background-color']
        self.atributos_region = ['id', 'top', 'bottom', 'left', 'right']
        self.atributos_img = ['src', 'region', 'begin', 'dur']
        self.atributos_audio = ['src', 'begin', 'dur']
        self.atributos_textstream = ['src', 'region']
        
        self.dicc_rlayout = {}
        self.dicc_region = {}
        self.dicc_img = {}
        self.dicc_audio = {}
        self.dicc_textstream = {}
        
        self.lista_etiqs = [self.dicc_rlayout, self.dicc_region, self.dicc_img,
                            self.dicc_audio, self.dicc_textstream]
                            
        
    def startElement(self, name, attrs):
        '''Método empleado al abrir una etiqueta'''
        
        if name == 'root-layout':
            for atributo in self.atributos_rlayout:
                self.dicc_rlayout[atributo] = attrs.get(atributo, '')
        if name == 'region':
            for atributo in self.atributos_region:
                self.dicc_region[atributo] = attrs.get(atributo, '')
        if name == 'img':
            for atributo in self.atributos_img:
                self.dicc_img[atributo]=attrs.get(atributo,'')
        if name == 'audio':
            for atributo in self.atributos_audio:
                self.dicc_audio[atributo] = attrs.get(atributo, '')
        if name == 'textstream':
            for atributo in self.atributos_textstream:
                self.dicc_textstream[atributo] = attrs.get(atributo, '')
                
if __name__ == '__main__':

    parser = make_parser()
    shandler = SmallSMILHandler()
    parser.setContentHandler(shandler)
    parser.parse(open('karaoke.smil'))
