#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Janssen:
 
    def extract_disease_to_be_treated(self, str):
        try:
           text = str.split('INDICA\xc3\x87\xc3\x95ES\n')[1]
           text = text[1:len(text)]
           text = text.split('RESULTADOS DE EFIC\xc3\x81CIA')[0]
           return text
        except:
           return ""