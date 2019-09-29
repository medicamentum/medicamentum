#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import mysql.connector
import sys
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


def extract_text(content, laboratory):
    content = content.encode('utf-8', 'ignore')

    text = ''

    if laboratory == 'EMS S/A':
        text = labs.ems.EMS().extract_disease_to_be_treated(content.decode())

    return text


mydb = mysql.connector.connect(
    host=sys.argv[1],
    user=sys.argv[2],
    passwd=sys.argv[3],
    database='DRUGS',
    use_unicode=True,
    charset='utf8mb4'
)

select_sql = 'SELECT A.leaflet, A.content, B.laboratory FROM DRUG_LEAFTLET A INNER JOIN DRUG B ON A.leaflet = B.leaflet'

select_cursor = mydb.cursor(buffered=True)
insert_cursor = mydb.cursor(buffered=True)

select_cursor.execute(select_sql)

for (leaflet, content, laboratory) in select_cursor:
    text = extract_text(content, laboratory)
    text = text.strip()

    if text == '':
        print(leaflet)
    else:
        try:
            insert_sql = 'INSERT into DRUG_DISEASE (leaflet, disease) values (%s, %s) '
            val = (leaflet,  text)
            insert_cursor.execute(insert_sql, val)
            mydb.commit()
        except:
            print(text)

insert_cursor.close()
select_cursor.close()
mydb.close()
