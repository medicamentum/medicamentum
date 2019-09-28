#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Accord:
 
    def extract_disease_to_be_treated(self, str):
        try:
           text = str.split('PARA QUE ESTE MEDICAMENTO \xC3\x89 INDICADO?')[1]
           text = text[1:len(text)]
           text = text.split('BULA PARA PACIENTE')[0]
           return text
        except:
           return ""