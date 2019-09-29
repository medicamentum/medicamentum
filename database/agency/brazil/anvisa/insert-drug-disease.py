#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import mysql.connector
import re

import labs.eurofarma
import labs.globo
import labs.ems
import labs.chron
import labs.legrand
import labs.baxter
import labs.biolabl
import labs.janssen
import labs.isofarma
import labs.accord


def extract_text(str):  # PUB/SUB will be better
    str = str.encode('utf-8', 'ignore')
    text = labs.eurofarma.Eurofarma().extract_disease_to_be_treated(str)
    if (text == ""):
        text = labs.ems.EMS().extract_disease_to_be_treated(str)
    if (text == ""):
        text = labs.ems.EMS().extract_disease_to_be_treated(str)
    if (text == ""):
        text = labs.biolabl.Biolab().extract_disease_to_be_treated(str)
    if (text == ""):
        text = labs.janssen.Janssen().extract_disease_to_be_treated(str)
    if (text == ""):
        text = labs.isofarma.Isofarma().extract_disease_to_be_treated(str)
    if (text == ""):
        text = labs.accord.Accord().extract_disease_to_be_treated(str)

    # if (text == "") :
    #    text = labs.globo.Globo().extract_disease_to_be_treated(str)
    # if (text == "") :
    #    text = labs.chron.Chron().extract_disease_to_be_treated(str)
    # if (text == "") :
    #    text = labs.legrand.Legrand().extract_disease_to_be_treated(str)
    # if (text == "") :
    #    text = labs.baxter.Baxter().extract_disease_to_be_treated(str)

    return text


mydb = mysql.connector.connect(
    host=sys.argv[1],
    user=sys.argv[2],
    passwd=sys.argv[3],
    database="DRUGS",
    use_unicode=True,
    charset='utf8mb4'
)

select_sql = "SELECT leaflet, content FROM DRUG_LEAFTLET"

select_cursor = mydb.cursor(buffered=True)
insert_cursor = mydb.cursor(buffered=True)

select_cursor.execute(select_sql)

for (leaflet, content) in select_cursor:
    text = extract_text(content)
    if (text == ""):
        print(leaflet)
    else:
        try:
            insert_sql = "INSERT into DRUG_DISEASE (leaflet, disease) values (%s, %s) "
            val = (leaflet, text)
            insert_cursor.execute(insert_sql, val)
            mydb.commit()
        except:
            print(text)

insert_cursor.close()
select_cursor.close()
mydb.close()
