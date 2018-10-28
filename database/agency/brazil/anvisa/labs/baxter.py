#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Baxter():

    def extract_disease_to_be_treated(self, str):
        try:
           text = str.split('INDICAÇÕES')[1]
           text = text[1:len(text)]
           text = text.split('CARACTERÍSTICAS FARMACOLÓGICAS')[0]
           return text
        except:
           return ""