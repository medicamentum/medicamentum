#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Biolab():

    def extract_disease_to_be_treated(self, str):
        try:
           text = str.split('1.\n\nINDICA\xc3\x87\xc3\x95ES')[1]
           text = text.split('2.\n\nRESULTADOS DE EFIC\xc3\x81CIA')[0]
           return text.strip()
        except:
           return ""