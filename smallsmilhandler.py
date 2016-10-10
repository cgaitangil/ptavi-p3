#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):
    '''Clase para extraer la información relevante del fichero XML'''

    def __init__(self):

        self.atrs_rlayout = ['etiqueta', 'width', 'height', 'background-color']
        self.atrs_region = ['etiqueta', 'id', 'top', 'bottom', 'left', 'right']
        self.atrs_img = ['etiqueta', 'src', 'region', 'begin', 'dur']
        self.atrs_audio = ['etiqueta', 'src', 'begin', 'dur']
        self.atrs_textstream = ['etiqueta', 'src', 'region']

        self.dicc_aux = {}
# 1 dicc por cada etiqueta, que se vaciara cuando pasemos a la sig. etiqueta

        self.lista_etiqs = []   # Donde guardaremos los dicc_aux

    def startElement(self, name, attrs):
        '''Método empleado al abrir una etiqueta'''

        if name == 'root-layout':
            for atributo in self.atrs_rlayout:
                if atributo == 'etiqueta':
                    self.dicc_aux[atributo] = name
                else:
                    self.dicc_aux[atributo] = attrs.get(atributo, '')
                # print(atributo + ' --> ' + str(self.dicc_aux[atributo]))
                # print('')
            self.lista_etiqs.append(self.dicc_aux)
            self.dicc_aux = {}  # Vaciamos para usarlo en la sig. etiqueta

        if name == 'region':
            for atributo in self.atrs_region:
                if atributo == 'etiqueta':
                    self.dicc_aux[atributo] = name
                else:
                    self.dicc_aux[atributo] = attrs.get(atributo, '')
                # print(atributo + ' --> ' + str(self.dicc_aux[atributo]))
                # print('')
            self.lista_etiqs.append(self.dicc_aux)
            self.dicc_aux = {}

        if name == 'img':
            for atributo in self.atrs_img:
                if atributo == 'etiqueta':
                    self.dicc_aux[atributo] = name
                else:
                    self.dicc_aux[atributo] = attrs.get(atributo, '')
                # print(atributo + ' --> ' + str(self.dicc_aux[atributo]))
                # print('')
            self.lista_etiqs.append(self.dicc_aux)
            self.dicc_aux = {}

        if name == 'audio':
            for atributo in self.atrs_audio:
                if atributo == 'etiqueta':
                    self.dicc_aux[atributo] = name
                else:
                    self.dicc_aux[atributo] = attrs.get(atributo, '')
                # print(atributo + ' --> ' + str(self.dicc_aux[atributo]))
                # print('')
            self.lista_etiqs.append(self.dicc_aux)
            self.dicc_aux = {}

        if name == 'textstream':
            for atributo in self.atrs_textstream:
                if atributo == 'etiqueta':
                    self.dicc_aux[atributo] = name
                else:
                    self.dicc_aux[atributo] = attrs.get(atributo, '')
                # print(atributo + ' --> ' + str(self.dicc_aux[atributo]))
                # print('')
            self.lista_etiqs.append(self.dicc_aux)
            self.dicc_aux = {}

    def get_tags(self):
        return self.lista_etiqs

if __name__ == '__main__':

    parser = make_parser()
    shandler = SmallSMILHandler()
    parser.setContentHandler(shandler)
    parser.parse(open('karaoke.smil'))
    print(shandler.lista_etiqs)
