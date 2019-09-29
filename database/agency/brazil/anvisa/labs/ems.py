#!/usr/bin/env python
# -*- coding: utf-8 -*-
class EMS():

    def extract_disease_to_be_treated(self, str):
        try:
            text = str.split('PARA QUE ESTE MEDICAMENTO')[1]
            text = text[11:len(text)]
            text = text.split('COMO ESTE MEDICAMENTO FUNCIONA')[0]
            return text
        except:
            try:
                text = str.split('PARA QUE ESSE MEDICAMENTO')[1]
                text = text[11:len(text)]
                text = text.split('COMO ESTE MEDICAMENTO FUNCIONA')[0]
                return text
            except:
                try:
                    text = str.split('ESTE MEDICAMENTO')[1]
                    text = text[11:len(text)]
                    text = text.split('COMO ESTE MEDICAMENTO FUNCIONA')[0]
                    return text
                except:
                    return ''
