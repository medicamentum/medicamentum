#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Legrand:
 
    def extract_disease_to_be_treated(self, str):
        try:
           text = str.split('1.INDICA')[1]
           text = text[1:len(text)]
           text = text.split('2. RESULTADOS DE EFIC')[0]
           return text
        except:
           return ""