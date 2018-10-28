#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Globo:
 
    def extract_disease_to_be_treated(self, str):
        try:
           text = str.split('1. PARA QUE ESTE MEDICAMENTO')[1]
           text = text[12:len(text)]
           text = text.split('2. COMO ESTE MEDICAMENTO FUNCIONA')[0]
           return text
        except:
           return ""