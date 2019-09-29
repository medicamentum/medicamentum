#!/usr/bin/env python
import glob
import sys
import os
import io
import mysql.connector
import unicodedata

mydb = mysql.connector.connect(
  host=sys.argv[1],
  user=sys.argv[2],
  passwd=sys.argv[3],
  database="DRUGS",
  use_unicode=True,
  charset='utf8'
)

path = sys.argv[4] + "/*.txt"

mycursor = mydb.cursor()

for file in glob.glob(path):

    content = io.open(file, mode="r", encoding="utf-8").read()
    content = content.strip()
    content = unicodedata.normalize("NFKC", content)

    directory, filename = os.path.split(file)
    filename = filename.replace(".txt", "")
    sql = "INSERT INTO DRUG_LEAFTLET (leaflet, content) VALUES (%s, %s)"
    val = (filename, content)
    print(filename, " processing ...")
    mycursor.execute(sql, val)
    mydb.commit()

print("Done")