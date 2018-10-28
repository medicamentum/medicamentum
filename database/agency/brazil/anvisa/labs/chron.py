#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Chron():

    def extract_disease_to_be_treated(self, str):
        try:
           text = str.split('PARA QUE ESTE MEDICAMENTO')[1]
           text = text[1:len(text)]
           text = text.split('COMO ESTE MEDICAMENTO FUNCIONA')[0]
           return text
        except:
           return ""