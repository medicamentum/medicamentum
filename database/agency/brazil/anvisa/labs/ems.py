#!/usr/bin/env python
# -*- coding: utf-8 -*-
class EMS():

    def extract_disease_to_be_treated(self, str):
        try:
           text = str.split('1. PARA QUE ESTE MEDICAMENTO \xc3\x89 INDICADO?')[1]
           text = text[4:len(text)]
           text = text.split('2. COMO ESTE MEDICAMENTO FUNCIONA?')[0]
           return text
        except:
           return ""